# استيراد مكتبه باند اس
import pandas as pd

# استيراد مكتبه الرسم
import matplotlib.pyplot as plt

from get_users_profiles import get_users_profiles

def show_users_age_density():

    # جلب بيانات المستخدمين من قاعدة البيانات
    df_profile = get_users_profiles()

    # استخراج عمود الأعمار
    df_age = df_profile['age']

    # إنشاء المخطط البياني للكثافة
    df_age.plot(kind='density')

    # تسمية المحاور والعنوان
    plt.xlabel("Age")  # المحور السيني يمثل العمر
    plt.ylabel("Density")  # المحور الصادي يمثل الكثافة
    plt.title("Users Age Density")  # عنوان المخطط

    # عرض المخطط
    plt.show()


show_users_age_density()