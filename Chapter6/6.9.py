def footToMeter(foot):
    meter = 0.305 * foot
    return meter 

def meterToFoot(meter):
    foot = meter / 0.305
    return foot

print("Feet\t Meters\t|\t Meters\t Feet")
print()


def main():
    i = 1.0
    r = 20.0
    while i < 11.0 and r < 67.0 :
        print(float(i),"\t",format(footToMeter(i),".3f"),"\t|\t",float(r),"\t",format(meterToFoot(r),".3f"))
        i += 1.0
        if r % 10 == 6 :
            r += 4.0
        else :
            r += 6.0
main()
    

    
    
