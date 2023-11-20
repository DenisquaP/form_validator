import re


async def type_of(val: str) -> str:
    date_formats = (
        # DD.MM.YYYY
        (r"^\d{2}\.\d{2}\.\d{4}$"),
        # YYYY-MM-DD
        (r"^\d{4}\-\d{2}\-\d{2}$"),
    )
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    phone_patterm = r"\+7\d{3}\d{3}\d{2}\d{2}"
    for i in date_formats:
        if re.fullmatch(i, val):
            return "date"
    if re.fullmatch(phone_patterm, val):
        return "phone"
    elif re.fullmatch(email_pattern, val):
        return "email"
    return "text"
