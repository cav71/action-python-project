from acbox.ureporting import Record, S, check


@check
def hello() -> Record:
    return Record(S.WARN, "hello", "wow")


@check
def world_one() -> Record:
    return Record(S.OK, "world", "one", index=0)


@check
def world_two() -> Record:
    return Record(S.WARN, "world", "two", index=1)


@check
def world_three() -> Record:
    return Record(S.FAILED, "world", "three", index=2)


@check
def world_four() -> Record:
    return Record(S.NOSTATUS, "world", "four", "a message", index=3)
