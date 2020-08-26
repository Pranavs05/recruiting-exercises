def allocation(order,inventory_distribution):
        
        """
        :param order: dict
        :param inventory_distribution: List[dict]
        :return: bestshipment : List[dict]
        """
        bestshipment=[]                                        # Stores the final best shipment
        temp=dict()                                            # Stores current warehouse asssigned for order
        flag=0                                                 # Indicates order not fulfilled for flag==1
        for item,quantity in order.items():
            startquantity=quantity
            for warehouse in inventory_distribution:
                    if item in warehouse['inventory']  and warehouse['inventory'][item]>0:      # checks if cuurent item is in warehouse
                        temp={}
                        if warehouse['inventory'][item] >= quantity:                           # if item quantity in warehouse greater than required quantity , required quantity is satisfied and hence is made zero
                            temp[warehouse['name']]={item:quantity}             
                            warehouse['inventory'][item] = warehouse['inventory'][item] - quantity
                            quantity = 0
                        else:
                            quantity=quantity-warehouse['inventory'][item]                      # if item quantity in warehouse less than required quantity, reduce requred quantity by what is available in warehouse
                            temp[warehouse['name']]={item:warehouse['inventory'][item]}
                            warehouse['inventory'][item] = 0

                        bestshipment.append(temp)
                    if quantity==0:
                        break
            if quantity == startquantity:          # if block checks if item quantity is same as start quantity , to verify if items exists in complete inventory
                break
            if quantity and quantity!=startquantity:  # set flag to check if order not fulfilled completely, this if block checks if quantity is not zero after checking all warehouses
                flag=1
                break
                
        if flag==1:                                    # Flag 1 indicates required quantity is not  available for the item ,  return empty list all and assigned orders are nullified
            bestshipment=[]
        bestshipment = sorted(bestshipment, key=lambda k: list(k.keys())) 
        return (bestshipment)  
        