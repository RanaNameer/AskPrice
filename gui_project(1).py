from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
from urlgenerator import *
import xlsxwriter

def gui():
    workbook = xlsxwriter.Workbook("Ask Price.xlsx")
    worksheet = workbook.add_worksheet("Data")
    worksheet.insert_image('I2', 'askprice.png')
    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})
    # Use the worksheet object to write 
    # data via the write() method.
    worksheet.write("G7", "Sr. No", bold)
    worksheet.write("H7", "Prduct Title", bold)
    worksheet.write("M7", "Product Price", bold)

    def getprice(url):
        headers = {"User-Agent" :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
        page = requests.get(url, headers = headers)
        soup1 = BeautifulSoup(page.content, "html.parser")
        soup2 = BeautifulSoup(soup1.prettify(),"html.parser")
        price = soup2.find(id="priceblock_ourprice").get_text()
        title = soup2.find(id="productTitle").get_text()
        (a,b)=(title,price)
        worksheet.write(f"G{c+8}", c+1)
        worksheet.write(f"H{c+8}", a)
        worksheet.write(f"M{c+8}", b)
    
    
    def parser():
        global c
        c = 0
        for i in [" amazon.co.uk", " amazon.ae"]:
            product = entry.get()
            user = product+i
            x = userinput(user)
            for url in x:
                try:
                    getprice(url)
                    c+=1
                except:
                    continue
            
        if c==0:
                messagebox.showinfo("Output","No product found")
        else:
                label1 = Label(window, text="{} resuls found".format(c))
                label1.grid(row=501, column=501)
                messagebox.showinfo("Output","Excel file created")
            
        workbook.close()

    window = Tk()
    window.title("Ask Price")
    window.geometry("500x200")
    photo = PhotoImage(file="askprice.png")
    label_1 = Label(window,image=photo,bg="white")
    label_1.grid(row=100,column=500, rowspan=5, columnspan=5)
    label = Label(window, text="Enter name of product", bg="white")
    label.grid(row=650, column=500)
    entry = Entry(window)
    entry.grid(row=650, column=501)
    button = Button(window, text="Search",  bg='blue', fg='black',command = parser)
    button.grid(row=651, column=502)
    button1 = Button(window, text="Quit", command=window.destroy)
    button1.grid(row=651, column=503)
    window.mainloop()

gui()
