from brownie import FundMe, accounts, network, exceptions
from brownie.network import account
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me
import pytest


def test_deploy():
    testing = deploy_fund_me()
    tx = testing
    tx


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    added_fee = 999887760000000000
    total_fee = entrance_fee + added_fee
    float_total_fee = float(total_fee)
    print(f"{entrance_fee} Is the entry fee from the getEnteranceFee() function.\n")
    print(f"{added_fee} Is a fee added for testing the withdraw() function.\n")
    print(f"The current total entry fee is {total_fee} wei\n")
    print(f"Now Funding Contract#: {fund_me} with {float_total_fee} (ETH)\n")
    tx2 = fund_me.fund({"from": account, "value": total_fee})
    tx2


def withdraw():
    print("\nNow Starting Withdraw Process...\n")
    fund_me = FundMe[-1]
    account = get_account()
    print(f"{fund_me} is the contract being withdrawn from..\n")
    print(f"{account} is the account funds will be deposited in.\n")
    tx3 = fund_me.withdraw({"from": account})
    tx3.wait(1)


def bad_transaction():
    fund_me = FundMe[-1]
    account = get_account()
    print(fund_me)
    print(account)
    # Warning: 'accounts.add()' will print memonic of new account to console.
    bad_actor = accounts.add()
    print(bad_actor)
    with pytest.raises(exceptions.VirtualMachineError):
        tx4 = fund_me.withdraw({"from": bad_actor})
        tx4.wait(1)


def mult_deploy_self():
    test_deploy()
    i = 1
    while i < 101:
        print(f"\n\nFund & Withdraw Iteration #: {i} out of 100\n")
        fund()
        withdraw()
        i += 1


def main():
    mult_deploy_self()

    # bad_transaction()
    # only run bad_transaction() on ganache-cli or other test enviornment. NOT TEST-NET(s)
