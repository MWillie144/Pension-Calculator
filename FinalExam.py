# Matthew Willie

from tkinter import *


class Pension:

    def __init__(self):
        window = Tk()
        window.title("Pension")

        # Labels
        lblSalaries = Label(window, text="Three\nHighest\nAnnual\nSalaries")
        lblSalaries.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        lblAge = Label(window, text="Age:")
        lblAge.grid(row=1, column=0, padx=5, pady=0, sticky=NE)

        lblService = Label(window, text="Service")
        lblService.grid(row=0, column=2, columnspan=2, padx=0, pady=5, sticky=N)

        lblYears = Label(window, text="Years:")
        lblYears.grid(row=0, column=2, columnspan=2, padx=0, pady=5)

        lblMonths = Label(window, text="Months:")
        lblMonths.grid(row=0, column=2, columnspan=2, padx=0, pady=5, sticky=S)

        lblPension = Label(window, text="Pension:")
        lblPension.grid(row=5, column=1, padx=5, pady=5)

        # Entries

        self.entrySalOne = StringVar("")
        entSalary1 = Entry(window, width=10, text=self.entrySalOne)
        entSalary1.grid(row=0, column=1, padx=0, pady=(5, 0), sticky=NW)

        self.entrySalTwo = StringVar("")
        entSalary2 = Entry(window, width=10, text=self.entrySalTwo)
        entSalary2.grid(row=0, column=1, padx=0, pady=0, sticky=W)

        self.entrySalThree = StringVar("")
        entSalary3 = Entry(window, width=10, text=self.entrySalThree)
        entSalary3.grid(row=0, column=1, padx=0, pady=(0, 5), sticky=SW)

        self.entryAge = StringVar("")
        entAge = Entry(window, width=2, text=self.entryAge)
        entAge.grid(row=1, column=1, padx=0, pady=0, sticky=NW)

        self.entryYears = StringVar("")
        entYears = Entry(window, width=2, text=self.entryYears)
        entYears.grid(row=0, column=3, padx=(0, 10), pady=0, sticky=W)

        self.entryMonths = StringVar("")
        entMonths = Entry(window, width=2, text=self.entryMonths)
        entMonths.grid(row=0, column=3, padx=(0, 10), pady=(0, 5), sticky=SW)

        self.conOfAnswer = StringVar("")
        entAnswer = Entry(window, width=15, state="readonly", textvariable=self.conOfAnswer)
        entAnswer.grid(row=5, column=2, padx=0, pady=5)

        # Button
        btnClear = Button(window, text="Clear Input", command=self.ClearInput)
        btnClear.grid(row=4, column=0, padx=(10, 0), pady=0, sticky=E)

        btnCalculate = Button(window, text="Calculate Pension", command=self.Calculate)
        btnCalculate.grid(row=4, column=1, columnspan=4, padx=10, pady=0, sticky=EW)

        btnClose = Button(window, text="Close Form", command=window.destroy)
        btnClose.grid(row=5, column=0, padx=(10, 0), pady=5, sticky=E)

        window.mainloop()

    # Creates an error message popup box
    def PopupMsg(self, box):
        alert = Tk()
        alert.wm_title("Error")
        lblError = Label(alert, width=25, text="{0}".format(box))
        lblError.grid(row=0, column=0, padx=25, pady=5)
        btnClose = Button(alert, text="OK", command=alert.destroy)
        btnClose.grid(row=1, column=0, padx=25, pady=5, sticky=EW)
        alert.mainloop()

    # Clears the Entry Boxes
    def ClearInput(self):
        self.entrySalOne.set("")
        self.entrySalTwo.set("")
        self.entrySalThree.set("")
        self.entryAge.set("")
        self.entryYears.set("")
        self.entryMonths.set("")
        self.conOfAnswer.set("")

    # Takes the user input and calculates pension
    # Checks to make sure inputs are valid
    # Outputs correct error message based on error
    def Calculate(self):
        # First Salary Box
        salary1 = self.entrySalOne.get()
        if (salary1.replace('-', '').isdecimal()):
            salary1 = float(salary1)
        elif (len(salary1) > 0):
            self.PopupMsg("Highest salary input\nmust be numeric.")
        else:
            self.PopupMsg("No input provided for\nhighest salary.")
        if (salary1 < 0):
            self.PopupMsg("Highest salary was invalid\nbecause it was negative.")

        # Second Salary Box
        salary2 = self.entrySalTwo.get()
        if (salary2.replace('-', '').isdecimal()):
            salary2 = float(salary2)
        elif (len(salary2) > 0):
            self.PopupMsg("Second highest salary input\nmust be numeric.")
        else:
            self.PopupMsg("No input provided for\nsecond highest salary.")
        if (salary2 < 0):
            self.PopupMsg("Second highest salary was invalid\nbecause it was negative.")

        # Third Salary Box
        salary3 = self.entrySalThree.get()
        if (salary3.replace('-', '').isdecimal()):
            salary3 = float(salary3)
        elif (len(salary3) > 0):
            self.PopupMsg("Third highest salary input\nmust be numeric.")
        else:
            self.PopupMsg("No input provided for\nthird highest salary.")
        if (salary3 < 0):
            self.PopupMsg("Third highest salary was invalid\nbecause it was negative.")

        # Age Box
        ageEntered = self.entryAge.get()
        if ageEntered.replace('-', '').isdigit():
            ageEntered = int(ageEntered)
        elif (len(ageEntered) > 0):
            self.PopupMsg("Age must be a whole number.")
        else:
            self.PopupMsg("No input provided for age.")
        if (ageEntered < 0):
            self.PopupMsg("Age was invalid\nbecause it was negative")

        # Years Box
        yearsEntered = self.entryYears.get()
        if yearsEntered.replace('-', '').isdigit():
            yearsEntered = int(yearsEntered)
        elif (len(yearsEntered) > 0):
            self.PopupMsg("Years must be a whole number.")
        else:
            self.PopupMsg("No input provided for years.")
        if (yearsEntered < 0):
            self.PopupMsg("Years was invalid\nbecause it was negative")

        # Months Box
        monthsEntered = self.entryMonths.get()
        if monthsEntered.replace('-', '').isdigit():
            monthsEntered = int(monthsEntered)
        elif (len(monthsEntered) > 0):
                self.PopupMsg("Months must be a whole number.")
        else:
                self.PopupMsg("No input provided for months.")
        if (monthsEntered < 0):
                self.PopupMsg("Months was invalid\nbecause it was negative")

        # Calculations for Pension
        else:
            ave = (salary1 + salary2 + salary3) / 3
            yrs = yearsEntered + (monthsEntered / 12)
            if (yrs >= 5):
                perRate = .075
                yrs -= 5
            else:
                perRate = yrs * .015
                yrs = 0
            if (yrs >= 5):
                perRate = .1625
                yrs -= 5
            else:
                perRate = perRate + (yrs * .0175)
                yrs = 0

            perRate = perRate + (yrs * .02)
            if (perRate > .80):
                p = .80
            else:
                p = perRate

            pension = p * ave
            self.conOfAnswer.set("${:,.2f}".format(float(pension)))


Pension()
