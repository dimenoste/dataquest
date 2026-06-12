import sys
from typing import Dict


def main() -> None:
    print("=== Inventory System Analysis ===\n")
    if len(sys.argv) < 2:
        print("Example usage : python3 ft_inventory_system.py \
              sword:1 potion:5 \
              shield:2 armor:3 \
              helmet:1 sword:2 hello key:value")
        return None
    list_items: list[str] = list()
    total: int = 0
    try:
        inventory: Dict[str, int] = dict()
        for i in range(1, len(sys.argv)):
            couple: list[str] = sys.argv[i].split(":")
            if len(couple) != 2:
                print(f"Error - invalid parameter {couple[0]}")
                continue
            else:
                x: str = couple[0]
                y: str = couple[1]
                if not x.isalpha():
                    print("Key must be only letters")
                    continue
                if x in list_items:
                    print(f"Redundant item {x} - discarding")
                    continue
                else:
                    list_items.append(x)
                try:
                    value_int = int(y)
                    inventory[x] = value_int
                    total += inventory[x]
                except Exception as e:
                    print(e)
                    continue
        if inventory and (len(inventory.keys()) <= 0):
            print("No proper key:value was found")
            return
        else:
            print(f"Got inventory : {inventory}")
            print(f"Item list: {list_items}")
            print(f"Total quantity of the {len(list_items)} :"
                  f"items :{list_items} : {total}")
            mini_key = list(inventory.keys())[0]
            maxi_key =  list(inventory.keys())[0]
            mini_value = inventory[mini_key]
            maxi_value = inventory[mini_key]
            for k, v in inventory.items():
                print(f"Item {k} represents {round(v/total * 100, 2)}%")
                if v < mini_value:
                    mini_value: int = v
                    mini_key: str = k
                if v > maxi_value:
                    maxi_value: int = v
                    maxi_key: str = k
            print(f"Item most abundant: {maxi_key} with quantity {maxi_value}")
            print(f"Item least abundant: {mini_key}"
                  f"with quantity {mini_value}")
            inventory.update({"magic_item": 1})
            print(f"Updated inventory: {inventory}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
