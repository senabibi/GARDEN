import math
def garden():
    print("This program will help you plan your garden.\nFirst,we need some information about dimensions you want.")
    leng4_f=float(input("\nPlease enter the side lenght for your garden (in feet):"))
    len1=(leng4_f)/4
    distance_i=float(input("Please enter the distance between plants (in inches):"))
    df=distance_i/12
    depth_flower_f=float(input("Please enter the depth for the flower beds (in feet):"))
    depth_fill_f=float(input("Please enter the depth for the fill (in feet):"))
    print("\nSummary of your plants needs.")
    each_tri_area=(2*(len1**2))
    each_tri_plant=each_tri_area/df**2
    all_tri_plants=int(each_tri_plant)*4
    print(f"Each outer triangular bed:{int(each_tri_plant)} plants.")
    cir_area=math.pi*(len1**2)
    cir_plant=(cir_area/df**2)
    print(f"The center circular bed:{int(cir_plant)} plants.")
    total_plants=all_tri_plants+cir_plant
    print(f"Total:{int(total_plants)} plants.")
    print("\nSummary of your soil needs.")
    each_tri_soil=((each_tri_area*depth_flower_f)/27)
    all_tri_soil=each_tri_soil*4
    print(f"Each outer triangular bed:{round(each_tri_soil,1)} cu. yd.")
    cir_soil=((cir_area*depth_flower_f)/27)
    print(f"The center circular bed:{round(cir_soil,1)} cu. yd.")
    all_soil=all_tri_soil+cir_soil
    print(f"Total:{round(all_soil,1)} cu. yd.")
    fill_area=(((leng4_f*leng4_f)-(each_tri_area*4)-(cir_area))*depth_fill_f)/27
    print("\nSummary of your soil needs.")
    print(f"Total:{round(fill_area,1)} cu. yd.")

garden()