def test_foo_file_exist(host):
    f = host.file("/etc/foo.conf")
    assert f.exists is True
    assert f.mode == 0o644