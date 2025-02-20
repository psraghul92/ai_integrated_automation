from pydantic import BaseModel


class ValidateLoginSuccessful(BaseModel):
    chart_icon_displayed: bool


class ValidateLoginFailure(BaseModel):
    error_message_displayed: bool
    error_message: str
