def mix(in_files: list[str], out_file: str):
    """
    averages the pixels of PPM images
    in_files is a list of input filenames
    out_file is the output filename
    """
    if not in_files:
        return

    in_streams = []
    first_prelude = None
    for f in in_files:
        in_streams.append(open("images/" + f, "r"))

        # first 3 lines of PPM files are:
        
        # encoding
        # width height
        # max color value
        
        # we don't actually need to pay attention to them,
        # but we do want to verify that they match
        prelude  = in_streams[-1].readline()
        prelude += in_streams[-1].readline()
        prelude += in_streams[-1].readline()

        if first_prelude is None:
            first_prelude = prelude
        else:
            assert prelude == first_prelude
    
    # record that prelude immediately
    with open("images/" + out_file, "w") as f:
        f.write(first_prelude)
    
    # we want to go line by line to save memory,
    # so append mode
    out = open("images/" + out_file, "a")

    cont = True
    while cont:
        # accumulate x,y,z for the same line from each file
        x_acc = 0
        y_acc = 0
        z_acc = 0

        for f in in_streams:
            line = f.readline()

            if line == "":
                # if we hit the end in any file, we're done
                cont = False
                break

            x, y, z = line.split(" ")

            x_acc += int(x)
            y_acc += int(y)
            z_acc += int(z)

        # exit before we write another line
        if not cont:
            break

        # average out values
        x_acc //= len(in_streams)
        y_acc //= len(in_streams)
        z_acc //= len(in_streams)
        
        # write them to output file
        out.write(f"{x_acc} {y_acc} {z_acc}\n")

    # clean everything up
    out.close()
    for f in in_streams:
        f.close()
