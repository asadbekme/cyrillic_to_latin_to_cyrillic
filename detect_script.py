import re

def detect_script(text: str) -> str:
    """
    Matndagi ustunlik qiluvchi alifboni aniqlaydi.
    Kiril harflari topilsa → 'cyrillic'
    Aks holda           → 'latin'
    """
    cyrillic_count = len(re.findall(r'[\u0400-\u04FF]', text))
    latin_count    = len(re.findall(r'[a-zA-Z]', text))

    if cyrillic_count > latin_count:
        return 'cyrillic'
    return 'latin'