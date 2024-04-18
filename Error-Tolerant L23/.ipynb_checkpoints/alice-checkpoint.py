class Alice:
    def __init__(self, bits_generator, basis_generator):
        self.bits = bits_generator()
        self.basis = basis_generator()
        self.shared_secret = ""
        self.INFO = []
        
    def generate_states_data(self, results):
        self.states_data = {}
        for i in range(len(results)):
            self.states_data[i] = results[i] + self.basis[i].lower()
    
    def is_f1_frame(self, frame):
        up, down = frame[0], frame[1]
        if (
            (self.states_data[up[0]] == "0x") and
            (self.states_data[up[1]] == "1z")
        ):
            return "Z"
        elif (
            (self.states_data[down[0]] == "1x") and
            (self.states_data[down[1]] == "0z")
        ):
            return "X"
        else:
            return False
        
    def is_f5_frame(self, frame):        
        up, down = frame[0], frame[1]
        if (
            (self.states_data[up[0]] == "1x") and
            (self.states_data[up[1]] == "0z")
        ):
            return "X"
        elif (
            (self.states_data[down[0]] == "0x") and
            (self.states_data[down[1]] == "1z")
        ):
            return "Z"
        else:
            return False
        
    def search_in_L_and_get_secret_bit(self, test_frame, L1, L2):
        # if test_frame is in L1
        if (test_frame in L1) or (test_frame[::-1] in L1):
            return "1"
        # if test_frame is in L2
        elif (test_frame in L2) or (test_frame[::-1] in L2):
            return "0"
        
    def calculate_bob_basis(self, L1, L2):
        pivots = []

        for i in range(len(L1)):
            if self.is_f1_frame(L1[i]):
                pivots.append(L1[i][0])
            elif self.is_f5_frame(L1[i]):
                pivots.append(L1[i][1])
                
        possible_secrets = [ [-1] * len(L1) for _ in range(len(pivots)) ]
        
        if L1:
            self.INFO.append((len(pivots), len(L1)))
        
        count = 0
        for pivot in pivots:
            for i in range(len(L1)):
                if pivot != L1[i][0]:
                    test_frame = (pivot, L1[i][0])
                    possible_secrets[count][i] = self.search_in_L_and_get_secret_bit(test_frame, L1, L2)
                else:
                    # if pivot == L1[i][0], we can conclude instantly? YES!
                    possible_secrets[count][i] = "0"
            possible_secrets[count] = ''.join(possible_secrets[count])
            count += 1

        self.shared_secret = possible_secrets
        return True