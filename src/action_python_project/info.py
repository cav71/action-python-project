import sys

from acbox.toolbox import info as acbox_info
from acbox.ureporting import load_external_checks, print_report


def main() -> int:
    report = []
    report.extend(acbox_info.check_sys("sys"))
    report.extend(acbox_info.check_plaform("platform"))
    report.extend(acbox_info.check_environ("environ.env"))
    report.extend(acbox_info.check_executables("environ.exe"))
    report.extend(acbox_info.check_envfile("envfile"))
    report.extend(load_external_checks(sys.argv[1:]))
    return print_report(report)


if __name__ == "__main__":
    sys.exit(main())
