from ipwndfu.main import SerialNumber, get_serial


def test_always_passes():
    assert True


def test_serial_number():
    sample = "CPID:8010 CPRV:11 CPFM:03 SCEP:01 BDID:0C ECID:[REDACTED-IDENTITY] IBFL:3C SRTG:[iBoot-2696.0.0.1.33]"

    serial = get_serial(sample)
    assert isinstance(serial, SerialNumber)
