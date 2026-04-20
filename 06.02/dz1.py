text = "Привіт! Як справи? Давно не бачились."
sentences = text.count('.') + text.count('!') + text.count('?')

print(f"Кількість речень: {sentences}")