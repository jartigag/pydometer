class Filter:

    COEFFICIENTS_LOW_0_HZ = {
        'alpha': [1, -1.979133761292768, 0.979521463540373],
        'beta':  [0.000086384997973502, 0.000172769995947004, 0.000086384997973502]
    }
    COEFFICIENTS_LOW_5_HZ = { # Direct form I, Chebyshev II, type = low-pass, Astop = 2, Fstop = 5, Fs = 100, Direct Form I
        'alpha': [1, -1.80898117793047, 0.827224480562408],
        'beta':  [0.095465967120306, -0.172688631608676, 0.095465967120306]
    }
    COEFFICIENTS_HIGH_1_HZ = { # Direct form I, Chebyshev II, type = high-pass, Fs = 100, Fstop = 0.5, Astop = 20, order = 2,
        'alpha': [1, -1.905384612118461, 0.910092542787947],
        'beta':  [0.953986986993339, -1.907503180919730, 0.953986986993339]
    }

    def low_0_hz(data):
        return Filter.filter(data, Filter.COEFFICIENTS_LOW_0_HZ)

    def low_5_hz(data):
        return Filter.filter(data, Filter.COEFFICIENTS_LOW_5_HZ)

    def high_1_hz(data):
        return Filter.filter(data, Filter.COEFFICIENTS_HIGH_1_HZ)

    def filter(data, coefficients):
        """Implementation of IIR (Infinite Impulse Response) filter:
        output_i = alpha_0 * (input_i*beta_0
                            + input_{i-1}*beta_1 + input_{i-2}*beta_2
                            + output{i-1}*alpha_1 + output_{i-2}*alpha_2)
        """

        filtered_data = [0,0]
        for i in range(2,len(data)):
            filtered_data.append( coefficients['alpha'][0] *
                (data[i]           * coefficients['beta'][0] +
                data[i-1]          * coefficients['beta'][1] +
                data[i-2]          * coefficients['beta'][2] -
                filtered_data[i-1] * coefficients['alpha'][1] -
                filtered_data[i-2] * coefficients['alpha'][2])
            )
        return filtered_data
