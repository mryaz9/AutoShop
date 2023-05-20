from typing import Union, TypeVar, Awaitable, Callable, Generic, Any, Optional

from aiogram.dispatcher.event.handler import FilterObject
from aiogram.enums import ContentType
from aiogram.types import Message
from aiogram_dialog import DialogProtocol, DialogManager
from aiogram_dialog.widgets.input import BaseInput
from aiogram_dialog.widgets.input.text import ManagedTextInputAdapter
from aiogram_dialog.widgets.widget_event import WidgetEventProcessor, ensure_event_processor

T = TypeVar("T")
TypeFactory = Callable[[str], T]
OnSuccess = Callable[[Message, "TextInput", DialogManager, T], Awaitable]
OnError = Callable[[Message, "TextInput", DialogManager], Awaitable]


class PhotoInput(BaseInput, Generic[T]):
    def __init__(
            self,
            id: str,
            type_factory: TypeFactory[T] = str,
            on_success: Union[OnSuccess[T], WidgetEventProcessor, None] = None,
            on_error: Union[OnError, WidgetEventProcessor, None] = None,
            filter: Optional[Callable[..., Any]] = None,
    ):
        super().__init__(id=id)
        if filter:
            self.filter = FilterObject(filter)
        else:
            self.filter = None
        self.type_factory = type_factory
        self.on_success = ensure_event_processor(on_success)
        self.on_error = ensure_event_processor(on_error)

    async def process_message(
            self,
            message: Message,
            dialog: DialogProtocol,
            manager: DialogManager,
    ):
        if message.content_type != ContentType.PHOTO:
            return False
        if self.filter and not await self.filter.call(
                manager.event, **manager.middleware_data,
        ):
            return False
        try:
            value = self.type_factory(message.text)
        except ValueError:
            await self.on_error.process_event(message, self, manager)
        else:
            # store original text
            self.set_widget_data(manager, message.photo[-1].file_id)
            await self.on_success.process_event(message, self, manager, value)
        return True

    def get_value(self, manager: DialogManager) -> T:
        return self.type_factory(self.get_widget_data(manager, None))

    def managed(self, manager: DialogManager):
        return ManagedTextInputAdapter(self, manager)
