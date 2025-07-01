from pydantic import BaseModel, EmailStr, constr, ConfigDict, field_validator
from datetime import datetime
from typing import Optional, Annotated
import pycountry
class UserBase(BaseModel):
    name: Annotated[str, constr(max_length=64)]
    last_name: Annotated[str, constr(max_length=64)]
    email: EmailStr
    card_number: Annotated[str, constr(max_length=16, min_length=13)]
    card_expiration: Annotated[str, constr(pattern=r"^(0[1-9]|1[0-2])\/\d{2}$")]
    card_cvv: Annotated[str, constr(min_length=3, max_length=4, pattern=r"^\d{3,4}$")]
    country: Annotated[str, constr(max_length=64)]
    city: Annotated[str, constr(max_length=64)]
    address: Annotated[str, constr(max_length=256)]
    postal_code: Annotated[str, constr(max_length=20)]
    phone: Annotated[str, constr(max_length=20)]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True, validate_by_name=True)
    @field_validator("country")
    def validate_country(cls, v):
        if not pycountry.countries.get(name=v) and not pycountry.countries.get(alpha_2=v) and not pycountry.countries.get(alpha_3=v):
            raise ValueError("Invalid country name or code")
        return v