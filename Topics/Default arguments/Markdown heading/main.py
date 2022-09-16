def heading(txt, lvl=1):
    if lvl < 1:
        lvl = 1
    elif lvl > 6:
        lvl = 6
    return f"{'#' * lvl} {txt}"
