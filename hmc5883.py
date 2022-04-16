
from msilib.schema import SelfReg


class HMC5883L:
    
    #PRE CONF FOR REGISTER A
    #CRA7(MSB)-CRA0(LSB)
    class REG_A:
        CRA_ADD = 0x00
        CRA_DEFAULT = 0x10
        #For tempature measurement CRA7 shoold be set but default 0
        TS_CRA7_Enable = 1 <<7
        TS_CRA7_Disable = 0 << 7#Default
        #CRA6 - CRA5 decide for samples avareged
        MA_CRA65_1=0<<5 #Default
        MA_CRA65_2=1<<5
        MA_CRA65_4=2<<5
        MA_CRA65_8=3<<5
        #CRA4 - CRA2 decide for samples avareged in Hz
        DO_CRA42_0HZ75 = 0<<2
        DO_CRA42_1HZ75 = 1<<2
        DO_CRA42_3HZ = 2<<2
        DO_CRA42_7HZ5 = 3<<2 #Default
        DO_CRA42_15HZ = 4<<2
        DO_CRA42_30HZ = 5<<2
        DO_CRA42_75HZ = 6<<2
        DO_CRA42_220HZ = 7<<2
        #CRA1 - CRA0 decide for Measurement Mode
        MS_CRA10_NORMAL = 0 #Default
        MS_CRA10_POS_BIAS = 1
        MS_CRA10_NEG_BIAS = 2
        MS_CRA10_TEMP_ONLY = 3
        #SET DEFAULT REGISTER VAL
        def __init__(self):
            self.CRA7=self.TS_CRA7_Disable 
            self.CRA65=self.MA_CRA65_1
            self.CRA42=self.DO_CRA42_7HZ5
            self.CRA10 =self.MS_CRA10_NORMAL
            self.DEFAULT_REG = self.CRA7 | self.CRA65 | self.CRA42 | self.CRA10
            pass
        def reset_reg(self):
            self.SPECIAL_REG = self.CRA_DEFAULT
        def set_reg(self, CRA7=TS_CRA7_Disable, CRA65=MA_CRA65_1, CRA42=DO_CRA42_7HZ5, CRA10 =MS_CRA10_NORMAL):
            self.SPECIAL_REG = CRA7 | CRA65 | CRA42 | CRA10
            pass
        def get_reg(self):
            return self.SPECIAL_REG
        def get_reg_add(self):
            return self.CRA_ADD

    #PRE CONF FOR REGISTER B
    class REG_B:
        CRB_ADD = 0x01
        CRB_DEFAULT = 0x20
        #it is gain dictionary for Register B
        #Tupple's first value represet firt three bits (MSB)
        #That is why shifted with 5
        #Second val of tupple represent digital resolution of out put
        GN_CRB75_0GA88 = (0 << 5, 0.73)
        GN_CRB75_1GA3 =  (1 << 5, 0.92) # Default
        GN_CRB75_1GA9 =  (2 << 5, 1.22)
        GN_CRB75_2GA5 =  (3 << 5, 1.52)
        GN_CRB75_4GA =  (4 << 5, 2.27)
        GN_CRB75_4GA7 = (5 << 5, 2.56)
        GN_CRB75_5GA6 = (6 << 5, 3.03)
        GN_CRB75_8GA1 = (7 << 5, 4.35)
        def __init__(self):
            self.CRB75=self.GN_CRB75_1GA3 
            self.CRB40='0b00000'
            self.DEFAULT_REG = self.CRB75(0) | self.CRB40(0)
            pass
        def reset_reg(self):
            self.SPECIAL_REG = self.CRB_DEFAULT
        def set_reg(self, CRB75=GN_CRB75_1GA3 ,CRA40='0b00000'):
            self.SPECIAL_REG = CRB75[0] | CRA40[0]
            pass
        def get_reg(self):
            return self.SPECIAL_REG
        def get_reg_add(self):
            return self.CRB_ADD
    
    class REG_MODE:
        MR_ADD = 0x02
        MR_DEFAULT = 0x20
        HS_MR7_ENABLE = 1<<7
        HS_MR7_DISABLE = 0<<7 #Default
        NA_MR6 = 0<<6 #Clear this bit for correct operation
        LP_MR5_ENABLE = 1<<5 #Lowest power mode. When set, ODR=0.75 Hz, and Averaging = 1
        LP_MR5_DISABLE = 0<<5
        NA_MR4 = 0<<4 #This bit has no functionality
        NA_MR3 = 0<<3 #Clear this bit for correct operation
        SPIM_MR2_4W = 0<<2
        SPIM_MR2_3W = 1<<2
        MD_MR10_CS = 0 #Continuous-Measurement Mode
        MD_MR10_SM = 1 #Single-Measurement Mode (Default)
        MD_MR10_IDLE = 2 #Idle Mode
        MD_MR10_IDLE = 3 #Idle Mode
        def __init__(self):
            self.MR7=self.HS_MR7_DISABLE 
            self.MR6=self.NA_MR6
            self.MR5=self.LP_MR5_DISABLE
            self.MR4=self.NA_MR4
            self.MR3=self.NA_MR3
            self.MR2=self.SPIM_MR2_4W
            self.MR10=self.MD_MR10_SM
            self.DEFAULT_REG = self.MR7 | self.MR6 | self.MR5 | self.MR4 | self.MR3 | self.MR2 | self.MR10
            pass
        def reset_reg(self):
            self.SPECIAL_REG = self.MR_DEFAULT
        def set_reg(self, MR7=HS_MR7_DISABLE, MR6=NA_MR6, MR5=LP_MR5_DISABLE, MR4=NA_MR4, MR3=NA_MR3, MR2=SPIM_MR2_4W, MR10=MD_MR10_SM):
            self.SPECIAL_REG = MR7 | MR6 | MR5 | MR4 | MR3 | MR2 | MR10
            pass
        def get_reg(self):
            return self.SPECIAL_REG
        def get_reg_add(self):
            return self.MR_ADD
    
    class REG_DXAB:
        def __init__(self):
            self.DXA_ADD = 0x03
            self.DXB_ADD = 0x04
            pass
        def get_reg_a_add(self):
            return self.DXA_ADD
        def get_reg_b_add(self):
            return self.DXB_ADD
    
    class REG_DYAB:
        def __init__(self):
            self.DYA_ADD = 0x05
            self.DYB_ADD = 0x06
            pass
        def get_reg_a_add(self):
            return self.DYA_ADD
        def get_reg_b_add(self):
            return self.DYB_ADD

    class REG_DZAB:
        def __init__(self):
            self.DZA_ADD = 0x07
            self.DZB_ADD = 0x08
            pass
        def get_reg_a_add(self):
            return self.DZA_ADD
        def get_reg_b_add(self):
            return self.DZB_ADD

    class REG_STATUS:
        def __init__(self):
            self.SR_ADD = 0x09
            pass
        def is_data_over_written(self,buff):
            return bool(buff & (1<<4))
        def is_data_output_reg_lock(self,buff):
            return bool(buff & (1<<1))
        def is_data_output_reg_rdy(self,buff):
            return bool(buff & 1)
        def get_reg_add(self):
            return self.SR_ADD

    class REG_IDENTIFICATION:
        #TODO
        pass

    class REG_DTEMPAB:
        #TODO
        pass
        

    def __init__(self,id=0, scl=4, sda=5, address=30, gauss='1.3', declination=(0, 0),freq=100000):
        self.reg_A = self.REG_A()
        self.reg_B = self.REG_B()
        self.reg_Mode = self.REG_MODE()
        self.reg_Dxab = self.REG_DXAB()
        self.reg_Dyab = self.REG_DYAB()
        self.reg_Dzab = self.REG_DZAB()
        self.reg_status = self.REG_STATUS()
        print(self.reg_A.get_addr()+' '+self.reg_B.get_addr())