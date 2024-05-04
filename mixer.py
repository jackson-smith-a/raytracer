def mix(in_files, out_file):
    """
    averages the pixels of PPM images
    in_files is a list of input filenames
    out_file is the output filename
    """
    if not in_files:
        return

    fs = []
    master_prelude = None
    for f in in_files:
        fs.append(open("images/" + f, "r"))
        prelude = ""
        prelude += fs[-1].readline()
        prelude += fs[-1].readline()
        prelude += fs[-1].readline()
        if master_prelude is None:
            master_prelude = prelude
        else:
            assert prelude == master_prelude
    
    with open("images/" + out_file, "w") as f:
        f.write(master_prelude)
        
    out = open("images/" + out_file, "a")

    cont = True
    while cont:
        x_acc = 0
        y_acc = 0
        z_acc = 0

        for f in fs:
            line = f.readline()
            if line == "":
                cont = False
                break
            x, y, z = line.split(" ")
            x_acc += int(x)
            y_acc += int(y)
            z_acc += int(z)
        if not cont:
            break
        x_acc //= len(fs)
        y_acc //= len(fs)
        z_acc //= len(fs)
        
        out.write(f"{x_acc} {y_acc} {z_acc}\n")

    out.close()
    for f in fs:
        f.close()
    
if __name__ == "__main__":
    mix(["image0.ppm", "image1.ppm"], "image.ppm")
