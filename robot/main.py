from parameters import Parameters
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    p = Parameters.load_from_file('./robot_params.json')
    print(p.pan_tilt_pins)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
