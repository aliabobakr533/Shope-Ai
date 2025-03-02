# استيراد مكتبه باند اس
import pandas as pd

# استيراد مكتبه الرسم
import matplotlib.pyplot as plt

from get_users_profiles import get_users_profiles


def show_users_age_hist():
    # عرض مخطط بياني (Histogram) يوضح توزيع أعمار المستخدمين.

    # جلب بيانات المستخدمين من قاعدة البيانات
    df_profile = get_users_profiles()

    # استخراج عمود الأعمار
    user_age = df_profile['age']

    # إنشاء المخطط باستخدام عدد معين من الفئات العمرية
    user_age.hist(bins=[0, 10, 20, 30, 40, 50, 60, 80])

    # تسمية المحاور والعنوان
    plt.xlabel('Age')  # المحور السيني يمثل العمر
    plt.ylabel('Count')  # المحور الصادي يمثل عدد المستخدمين
    plt.title('Users Age Histogram')  # عنوان المخطط

    # عرض المخطط
    plt.show()

show_users_age_hist()