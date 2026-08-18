def reconcile(local_orders: list[dict], broker_orders: list[dict]) -> dict:
    local = {str(item["id"]): item for item in local_orders}
    broker = {str(item["id"]): item for item in broker_orders}
    return {"missing_at_broker": sorted(set(local) - set(broker)),
            "unknown_at_broker": sorted(set(broker) - set(local)),
            "status_mismatches": sorted(order_id for order_id in set(local) & set(broker)
                                         if local[order_id].get("status") != broker[order_id].get("status"))}

