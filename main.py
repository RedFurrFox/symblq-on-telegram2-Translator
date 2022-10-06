def decode(text):
    dec_a = text.replace("𓂅", "a")
    dec_b = dec_a.replace("✦", "b")
    dec_c = dec_b.replace("✧", "c")
    dec_d = dec_c.replace("⊹", "d")
    dec_e = dec_d.replace("⋆", "e")
    dec_f = dec_e.replace("⌕", "f")
    dec_g = dec_f.replace("ꗃ", "g")
    dec_h = dec_g.replace("⋈", "h")
    dec_i = dec_h.replace("ഒ", "i")
    dec_j = dec_i.replace("୨୧", "j")
    dec_k = dec_j.replace("⌯", "k")
    dec_l = dec_k.replace("﹅", "l")
    dec_m = dec_l.replace("﹆", "m")
    dec_n = dec_m.replace("ଘ", "n")
    dec_o = dec_n.replace("ꕤ", "o")
    dec_p = dec_o.replace("ꔛ", "p")
    dec_q = dec_p.replace("𓏲ָ", "q")
    dec_r = dec_q.replace("ǂ", "r")
    dec_s = dec_r.replace("𓍼", "s")
    dec_t = dec_s.replace("ᯅ", "t")
    dec_u = dec_t.replace("ꮺ", "u")
    dec_v = dec_u.replace("⌗", "v")
    dec_w = dec_v.replace("ꉂ", "w")
    dec_x = dec_w.replace("ᨒ", "x")
    dec_y = dec_x.replace("๑", "y")
    dec_z = dec_y.replace("𐂯", "z")
    decoded = dec_z
    print(f'\nHere is Your Decoded Text:\n"{decoded}"')
    exit()

def encode(text):
    enc_a = text.replace("a", "𓂅")
    enc_b = enc_a.replace("b", "✦")
    enc_c = enc_b.replace("c", "✧")
    enc_d = enc_c.replace("d", "⊹")
    enc_e = enc_d.replace("e", "⋆")
    enc_f = enc_e.replace("f", "⌕")
    enc_g = enc_f.replace("g", "ꗃ")
    enc_h = enc_g.replace("h", "⋈")
    enc_i = enc_h.replace("i", "ഒ")
    enc_j = enc_i.replace("j", "୨୧")
    enc_k = enc_j.replace("k", "⌯")
    enc_l = enc_k.replace("l", "﹅")
    enc_m = enc_l.replace("m", "﹆")
    enc_n = enc_m.replace("n", "ଘ")
    enc_o = enc_n.replace("o", "ꕤ")
    enc_p = enc_o.replace("p", "ꔛ")
    enc_q = enc_p.replace("q", "𓏲ָ")
    enc_r = enc_q.replace("r", "ǂ")
    enc_s = enc_r.replace("s", "𓍼")
    enc_t = enc_s.replace("t", "ᯅ")
    enc_u = enc_t.replace("u", "ꮺ")
    enc_v = enc_u.replace("v", "⌗")
    enc_w = enc_v.replace("w", "ꉂ")
    enc_x = enc_w.replace("x", "ᨒ")
    enc_y = enc_x.replace("y", "๑")
    enc_z = enc_y.replace("z", "𐂯")
    encoded = enc_z
    print(f'\nHere is Your Encoded Text:\n"{encoded}"')
    exit()

def translator(text, type):
    if type == 1:
        decode(text=text)
    elif type == 2:
        encode(text=text)
    else:
        exit()


if __name__ == "__main__":
    print("""
█▀ █▄█ █▀▄▀█ █▀█ █░░ █▀█   █▀█ █▄░█ 
▄█ ░█░ █░▀░█ █▄█ █▄▄ ▀▀█   █▄█ █░▀█ 

▀█▀ █▀▀ █░░ █▀▀ █▀▀ █▀█ ▄▀█ █▀▄▀█   ▀█ 
░█░ ██▄ █▄▄ ██▄ █▄█ █▀▄ █▀█ █░▀░█   █▄ 

▀█▀ █▀█ ▄▀█ █▄░█ █▀ █░░ ▄▀█ ▀█▀ █▀█ █▀█
░█░ █▀▄ █▀█ █░▀█ ▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄

coded by: RedFurrFox On GitHub""")
    translator(
        type=int(input("\nChoices:\n[1] Decode\n[2] Encode\n[0] Exit\n>>> ")),
        text=input("\nPlease enter your text to be translated:\n>>> ")
    )
