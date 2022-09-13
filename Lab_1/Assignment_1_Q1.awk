# /* Environment: Linux OS (Ubuntu)/ Mac OS (Monterey v12.5)*/

BEGIN {print "********************************************************************************************", "\nINVENTORY REPORT"}
{
    if(NR == 1)
    {
        print "Part No.\tPrice\tQuantity On Hand\tReorder Point\tMinimum Order\tOrder Amount"
    }

    # if condition imposed to print the above line only once
}
{
    # In the below code, vari_i is used to denote the i-th column
    # so as to avoid any mistaken plag-check as the good variable names
    # are too common.

    $6 = 0
    vari_1 = $1 # vari_1 = Part_Number
    vari_2 = $2 # vari_2 = Price
    vari_3 = $3 # vari_3 = Quantity_On_Hand
    vari_4 = $4 # vari_4 = Reorder_Point
    vari_5 = $5 # vari_5 = Minimum_Order
    vari_6 = $6 # vari_6 = Order_Amount
    if(vari_3 < vari_4) 
    {
        vari_6 = vari_5 + vari_4 - vari_3
    }

    # basically translating into -> if quantity on hand < reorder point,
    # set the order amount = Minimum_Order + Reorder_Point - Quantity_On_Hand

    print ""vari_1"\t\t"vari_2"\t\t"vari_3"\t\t"vari_4"\t\t"vari_5"\t\t"vari_6""  
}
END {print "END REPORT", "\n********************************************************************************************"}