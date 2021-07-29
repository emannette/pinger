import pytest
from src import main
from src.exceptions import HostExceptions

class TestMainModule():
        
    def test_main_sanity_check(self):
        print('The "main" sanity check')
        assert True

    def test_getting_no_arguments(self):
        test_args = main.get_args()
        # breakpoint()
        assert test_args.host_file is None

    @pytest.mark.skip(reason='Unsure how to test passing arguments via command line.')
    def test_getting_file_argument(self):
        assert False

    def test_getting_hosts_with_no_hosts_file(self):
        with pytest.raises(HostExceptions.MissingHostsException):
            main.get_hosts(None)

    def test_getting_hosts_with_hosts_file(self):
        host_file = 'tests/lib/test_hosts.txt'
        hosts = main.get_hosts(host_file)
        assert len(hosts) == 6

    def test_getting_hosts_with_blank_hosts_file(self):
        # If no hosts are present in the file then we should get a MissingHostsException
        with pytest.raises(HostExceptions.MissingHostsException):
            host_file = 'tests/lib/empty_host_file.txt'
            _ = main.get_hosts(host_file)


