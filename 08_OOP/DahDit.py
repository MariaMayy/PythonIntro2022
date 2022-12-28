class morse:
    def __init__(self, pars = "", buf = "."):
        self.pars = pars
        self.buf = buf
        self.end = "."

        if (pars == ""):
            self.di = "di"
            self.dit = "dit"
            self.dah = "dah"
        else:
            cur = pars.split(" ")
            if (len(cur) == 1):
                self.end = ""
                self.di = cur[0][0]

                if (len(cur[0]) == 2):
                    self.dit = cur[0][0]
                    self.dah = cur[0][1]
                elif (len(cur[0]) == 3):
                    self.dit = cur[0][1]
                    self.dah = cur[0][2]
                else:
                    self.dit = cur[0][1]
                    self.dah = cur[0][2]
                    self.end = cur[0][3]
            elif (len(cur) == 2):
                self.di = cur[0]
                self.dit = cur[0]
                self.dah = cur[1]
            elif (len(cur) == 3):
                self.di = cur[0]
                self.dit = cur[1]
                self.dah = cur[2]
            else:
                self.di = cur[0]
                self.dit = cur[1]
                self.dah = cur[2]
                self.end = cur[3]
        
    def __str__(self):
        if ((len(self.pars.split(" ")) == 1) and (self.pars != "")):
            self.buf = self.buf.replace(self.di + ",", self.dit)
            self.buf = self.buf.replace(self.dah + ",", self.dah)
            self.buf = self.buf[:len(self.buf) - 1]

            if (self.buf[len(self.buf) - 1] == self.di):
                self.buf = self.buf[:len(self.buf) - 1] + self.dit + self.end
            else:
                self.buf = self.buf + self.end
        else:
            self.buf = self.buf.replace(self.di + " ,", self.dit + ",")
            self.buf = self.buf.replace(self.dah + " ,", self.dah + ",")
            self.buf = self.buf.replace(self.di + " .", self.dit + self.end)
            self.buf = self.buf.replace(self.dah + " .", self.dah + self.end)
        return self.buf

    def __neg__(self):
        if (len(self.pars.split(" ")) == 1 and (self.pars != "")):
            return morse(self.pars, self.dah + self.buf)
        else:
            return morse(self.pars, self.dah + " " + self.buf)

    def __pos__(self):
        if (len(self.pars.split(" ")) == 1 and (self.pars != "")):
            return morse(self.pars, self.di + self.buf)
        else:
            return morse(self.pars, self.di + " " + self.buf)

    def __invert__(self):
        return morse(self.pars, ", " + self.buf)
    
