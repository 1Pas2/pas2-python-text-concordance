import re


def concordance(text: str, case_sensitive: bool = False) -> dict[str, list[int]]:
    result = {}
    for match in re.finditer(r"[^\W_]+(?:[\x27’][^\W_]+)*", text, flags=re.UNICODE):
        word = match.group() if case_sensitive else match.group().casefold()
        result.setdefault(word, []).append(match.start())
    return result


def contexts(text: str, offsets, radius: int = 20) -> list[str]:
    if type(radius) is not int or radius < 0:
        raise ValueError("Invalid radius")
    result = []
    for offset in offsets:
        if type(offset) is not int or not 0 <= offset < len(text):
            raise ValueError("Invalid offset")
        result.append(
            text[max(0, offset - radius) : min(len(text), offset + radius + 1)]
        )
    return result
