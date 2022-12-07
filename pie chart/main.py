import matplotlib.pyplot as plt
import pandas as pd


def first():
    # Data to plot consists of  labels, sizes and colors for each # label
    #النصوص
    labels = 'Python', 'C++', 'Ruby', 'Java'
    #النسبة
    sizes = [215, 130, 245, 210]
    #الالوان
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

    explode = (0.1, 0, 0, 0)  # explode 1st slice# لابعاد اول شكل من الدائرة

    # Plot
    ''''
    pie(){
    دالة تستعمل لانشاء المخطط الدائري
    }
    
****** parameters   ************** 
    
    explode{
         Each value represents how far from the center each wedge is displayed
تمثل كل قيمة مدى بعد كل قطعة عن المركز         
    }
     
    
    startangle{
    يتم تعريف متغير startangle بزاوية بالدرجات ، الزاوية الافتراضية هي 0: 
     The startangle parameter is defined with an angle in degrees, default angle is 0:
    }
    shadow{
    Add a shadow to the pie chart
    تستعمل لاظهار ظل خلف المخطط
    }
    Colors{
    You can set the color of each wedge with the colors parameter.
    يمكنك ضبط لون كل قطعة باستخدام معلمة الألوان.
    }
    Legend {
    To add a list of explanation for each wedge
    لإضافة قائمة شرح لكل إسفين
    }
    counterclock{
    لتحديد اتجاه الكسور للمخطط الدائري ،
     يجب عليك تعيين معلمة عداد الساعة إلى صواب أو خطأ (القيمة هي صواب افتراضيا) 
    To specify fractions direction of the pie chart, you must set the counterclock parameter to True or False (value is True by default). 
    }
    
    '''
    plt.pie(sizes, explode=explode, labels=labels,
            colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=140,counterclock=False)

    plt.axis('equal')
    plt.title("pie chart")
    # Adding legend

    plt.legend()#to show small squre contain the data
    plt.legend(title="programing languages:")

    plt.show()


def second():
    # Data to plot consists of  labels, sizes and colors for each # label
    labels = 'Python', 'C++', 'Ruby', 'Java'
    sizes = [215, 130, 245, 210]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

    # Plot
    patches, texts = plt.pie(sizes, colors=colors, shadow=True,
                             startangle=90)

    plt.legend(patches, labels, loc="best")
    plt.axis('equal')

    plt.show()


second()