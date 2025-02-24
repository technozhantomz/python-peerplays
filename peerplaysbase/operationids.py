ops = [
    "transfer",
    "limit_order_create",
    "limit_order_cancel",
    "call_order_update",
    "fill_order",
    "account_create",
    "account_update",
    "account_whitelist",
    "account_upgrade",
    "account_transfer",
    "asset_create",
    "asset_update",
    "asset_update_bitasset",
    "asset_update_feed_producers",
    "asset_issue",
    "asset_reserve",
    "asset_fund_fee_pool",
    "asset_settle",
    "asset_global_settle",
    "asset_publish_feed",
    "witness_create",
    "witness_update",
    "proposal_create",
    "proposal_update",
    "proposal_delete",
    "withdraw_permission_create",
    "withdraw_permission_update",
    "withdraw_permission_claim",
    "withdraw_permission_delete",
    "committee_member_create",
    "committee_member_update",
    "committee_member_update_global_parameters",
    "vesting_balance_create",
    "vesting_balance_withdraw",
    "worker_create",
    "custom",
    "assert",
    "balance_claim",
    "override_transfer",
    "transfer_to_blind",
    "blind_transfer",
    "transfer_from_blind",
    "asset_settle_cancel",
    "asset_claim_fees",
    "fba_distribute",
    "tournament_create",
    "tournament_join",
    "game_move",
    "asset_update_dividend",
    "asset_dividend_distribution",
    "tournament_payout",
    "tournament_leave",
    "sport_create",
    "sport_update",
    "event_group_create",
    "event_group_update",
    "event_create",
    "event_update",
    "betting_market_rules_create",
    "betting_market_rules_update",
    "betting_market_group_create",
    "betting_market_create",
    "bet_place",
    "betting_market_group_resolve",
    "betting_market_group_resolved",
    "bet_adjusted",
    "betting_market_group_cancel_unmatched_bets",
    "bet_matched",
    "bet_cancel",
    "bet_canceled",
    "betting_market_group_update",
    "betting_market_update",
    "event_update_status",
    "sport_delete",
    "event_group_delete",
    "affiliate_payout",
    "affiliate_referral_payout",
    "lottery_asset_create",
    "ticket_purchase",
    "lottery_reward",
    "lottery_end",
    "sweeps_vesting_claim",
    "custom_permission_create",
    "custom_permission_update",
    "custom_permission_delete",
    "custom_account_authority_create",
    "custom_account_authority_update",
    "custom_account_authority_delete",
]
operations = {o: ops.index(o) for o in ops}


def getOperationNameForId(i):
    """ Convert an operation id into the corresponding string
    """
    for key in operations:
        if int(operations[key]) is int(i):
            return key
    return "Unknown Operation ID %d" % i
