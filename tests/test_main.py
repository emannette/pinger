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
        host_file = 'lib/test_hosts.txt'
        main.get_hosts(host_file)
        