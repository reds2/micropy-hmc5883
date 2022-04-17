
import machine
import utime

class REGISTERS:    
    #PRE CONF FOR REGISTER A
    #CRA7(MSB)-CRA0(LSB)
    class REG_A:
        CRA_ADD = 0x00
        CRA_DEFAULT_VAL = 0x10
        CRA_SPECIAL_VAL = CRA_DEFAULT_VAL
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
            self.CRA_DEFAULT_VAL = self.CRA7 | self.CRA65 | self.CRA42 | self.CRA10
        def reset_reg_val(self):
            self.CRA_SPECIAL_VAL = self.CRA_DEFAULT_VAL
        def set_reg_val(self, CRA7=TS_CRA7_Disable, CRA65=MA_CRA65_1, CRA42=DO_CRA42_7HZ5, CRA10 =MS_CRA10_NORMAL):
            self.CRA_SPECIAL_VAL = CRA7 | CRA65 | CRA42 | CRA10
        def get_reg_val(self):
            return self.CRA_SPECIAL_VAL
        def get_reg_add(self):
            return self.CRA_ADD

    #PRE CONF FOR REGISTER B
    class REG_B:
        CRB_ADD = 0x01
        CRB_DEFAULT_VAL = 0x20
        CRB_SPECIAL_VAL = CRB_DEFAULT_VAL
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
            self.CRB40= 0 << 4
            self.CRB_DEFAULT_VAL = self.GN_CRB75_1GA3[0] | self.CRB40
        def reset_reg_val(self):
            self.CRB_SPECIAL_VAL = self.CRB_DEFAULT_VAL
        def set_reg_val(self, CRB75=GN_CRB75_1GA3[0] ,CRA40=0 << 4):
            self.CRB_SPECIAL_VAL = CRB75[0] | CRA40
        def get_reg_val(self):
            return self.CRB_SPECIAL_VAL
        def get_reg_add(self):
            return self.CRB_ADD
    
    class REG_MODE:
        MR_ADD = 0x02
        MR_DEFAULT_VAL = 0x20
        MR_SPECIAL_VAL = MR_DEFAULT_VAL
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
            self.MR_DEFAULT_VAL = self.MR7 | self.MR6 | self.MR5 | self.MR4 | self.MR3 | self.MR2 | self.MR10
        def reset_reg_val(self):
            self.MR_SPECIAL_VAL = self.MR_DEFAULT_VAL
        def set_reg_val(self, MR7=HS_MR7_DISABLE, MR6=NA_MR6, MR5=LP_MR5_DISABLE, MR4=NA_MR4, MR3=NA_MR3, MR2=SPIM_MR2_4W, MR10=MD_MR10_SM):
            self.MR_SPECIAL_VAL = MR7 | MR6 | MR5 | MR4 | MR3 | MR2 | MR10
        def get_reg_val(self):
            return self.MR_SPECIAL_VAL
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
        def get_reg_a_val(self):
            #TODO
            pass
        def get_reg_b_val(self):
            #TODO
            pass
    
    class REG_DYAB:
        def __init__(self):
            self.DYA_ADD = 0x05
            self.DYB_ADD = 0x06
            pass
        def get_reg_a_add(self):
            return self.DYA_ADD
        def get_reg_b_add(self):
            return self.DYB_ADD
        def get_reg_a_val(self):
            #self.i2c_conn.start()
            #self.i2c_conn.readfrom_mem()
            pass
        def get_reg_b_val(self):
            #TODO
            pass

    class REG_DZAB:
        def __init__(self):
            self.DZA_ADD = 0x07
            self.DZB_ADD = 0x08
        def get_reg_a_val(self):
            #TODO
            pass
        def get_reg_b_val(self):
            #TODO
            pass
        def get_reg_a_add(self):
            return self.DZA_ADD
        def get_reg_b_add(self):
            return self.DZB_ADD

    class REG_STATUS:
        def __init__(self):
            self.SR_ADD = 0x09
            self.SR_DEFAULT_VAL = 0b00000000
        def is_data_over_written(self,buff):
            #TODO
            #return bool(buff & (1<<4))
            pass
        def is_data_output_reg_lock(self,buff):
            #TODO
            #return bool(buff & (1<<1))
            pass
        def is_data_output_reg_rdy(self,buff):
            #TODO
            #return bool(buff & 1)
            pass
        def get_reg_add(self):
            return self.SR_ADD

    class REG_IDENTIFICATION:
        def __init__(self):
            self.IRA_ADD = 0x0A
            self.IRA_DEFAULT_VAL = 0b01001000
            self.IRB_ADD = 0x0B
            self.IRB_DEFAULT_VAL = 0b00110100
            self.IRC_ADD = 0x0C
            self.IRC_DEFAULT_VAL = 0b00110011
        def get_reg_a_add(self):
            return self.IRA_ADD
        def get_reg_a_val(self):
            return self.IRA_DEFAULT_VAL
        def get_reg_b_add(self):
            return self.IRB_ADD
        def get_reg_b_val(self):
            return self.IRB_DEFAULT_VAL
        def get_reg_c_add(self):
            return self.IRC_ADD
        def get_reg_c_val(self):
            return self.IRC_DEFAULT_VAL
    def __init__(self,gauss='1.3', declination=(0, 0)):
        pass
        

class I2C_DRIVER(REGISTERS):
    def __init__(self,id=1, scl=15, sda=14, address=30,freq=100000):
        self.i2c_conn = machine.I2C(id=id,sda=machine.Pin(sda),scl=machine.Pin(scl),freq=freq)
        len_of_place_holder=17
        self.reg_A = self.REG_A()
        self.reg_B = self.REG_B()
        self.reg_Mode = self.REG_MODE()
        self.reg_Dxab = self.REG_DXAB()
        self.reg_Dyab = self.REG_DYAB()
        self.reg_Dzab = self.REG_DZAB()
        self.reg_status = self.REG_STATUS()
        #self.i2c_conn.start()
        self.i2c_conn.writeto_mem(address,self.reg_A.get_reg_add(),bin(self.reg_A.get_reg_val()))
        self.i2c_conn.writeto_mem(address,self.reg_B.get_reg_add(),bin(self.reg_B.get_reg_val()))
        self.i2c_conn.writeto_mem(address,self.reg_Mode.get_reg_add(),bin(self.reg_Mode.get_reg_val()))
        #self.i2c_conn.stop()
        print("\n",\
            "{:{}}".format("REGISTER NAME",len_of_place_holder),"{:3}".format(" "),"{:10}".format("ADDRESS"),"{:3}".format(" "),"{:10}".format("VALUE"),'\n',\
            "{:-^{}}".format("",len_of_place_holder+3+10+3+10),"\n",\
            "{:<{}}".format("REGISTER A",len_of_place_holder),"=> ","{:>08b}".format(self.reg_A.get_reg_add()),"{:3}".format(" "),"{:>08b}".format(self.reg_A.get_reg_val()),'\n',\
            "{:<{}}".format("REGISTER B",len_of_place_holder),"=> ","{:>08b}".format(self.reg_B.get_reg_add()),"{:3}".format(" "),"{:>08b}".format(self.reg_A.get_reg_val()),'\n',\
            "{:<{}}".format("REGISTER MODE",len_of_place_holder),"=> ","{:>08b}".format(self.reg_Mode.get_reg_add()),"{:3}".format(" "),"{:>08b}".format(self.reg_Mode.get_reg_val()),'\n',\
            "{:<{}}".format("REGISTER DXA",len_of_place_holder),"=> ","{:>08b}".format(self.reg_Dxab.get_reg_a_add()),"{:3}".format(" "),"{:>08b}".format(self.i2c_conn.readfrom_mem(address,self.reg_Dxab.get_reg_a_add(),1,addrsize=8)[0]),'\n',\
            "{:<{}}".format("REGISTER DXB",len_of_place_holder),"=> ","{:>08b}".format(self.reg_Dxab.get_reg_b_add()),"{:3}".format(" "),"{:>08b}".format(self.i2c_conn.readfrom_mem(address,self.reg_Dxab.get_reg_b_add(),1,addrsize=8)[0]),'\n',\
            "{:<{}}".format("REGISTER DYA",len_of_place_holder),"=> ","{:>08b}".format(self.reg_Dyab.get_reg_a_add()),"{:3}".format(" "),"{:>08b}".format(self.i2c_conn.readfrom_mem(address,self.reg_Dyab.get_reg_a_add(),1,addrsize=8)[0]),'\n',\
            "{:<{}}".format("REGISTER DYB",len_of_place_holder),"=> ","{:>08b}".format(self.reg_Dyab.get_reg_b_add()),"{:3}".format(" "),"{:>08b}".format(self.i2c_conn.readfrom_mem(address,self.reg_Dyab.get_reg_b_add(),1,addrsize=8)[0]),'\n',\
            "{:<{}}".format("REGISTER DZA",len_of_place_holder),"=> ","{:>08b}".format(self.reg_Dzab.get_reg_a_add()),"{:3}".format(" "),"{:>08b}".format(self.i2c_conn.readfrom_mem(address,self.reg_Dzab.get_reg_a_add(),1,addrsize=8)[0]),'\n',\
            "{:<{}}".format("REGISTER DZB",len_of_place_holder),"=> ","{:>08b}".format(self.reg_Dzab.get_reg_b_add()),"{:3}".format(" "),"{:>08b}".format(self.i2c_conn.readfrom_mem(address,self.reg_Dzab.get_reg_b_add(),1,addrsize=8)[0]),'\n',\
            "{:<{}}".format("REGISTER STATUS",len_of_place_holder),"=> ","{:>08b}".format(self.reg_status.get_reg_add()),"{:3}".format(" "),"{:>08b}".format(self.i2c_conn.readfrom_mem(address,self.reg_status.get_reg_add(),1,addrsize=8)[0]),'\n') 

    
    def read_data_regs(self):
        #TODO
        pass

    def write_config_mode(self):
        #TODO
        pass

    def read_status(self):
        #TODO
        pass