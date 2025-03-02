# استيراد المكتبات اللازمة للعمل مع البيانات وتحليلها

import pandas as pd  # مكتبة لتحليل البيانات ومعالجتها بسهولة
import matplotlib.pyplot as plt  # مكتبة لرسم المخططات البيانية
import seaborn as sns  # مكتبة لرسم المخططات الإحصائية بطريقة جذابة
import mysql.connector  # مكتبة للتعامل مع قواعد بيانات MySQL# استيراد المكتبات اللازمة للعمل مع البيانات وتحليلها


# تعريف دالة لإنشاء اتصال بقاعدة البيانات
def make_connection_with_db():
    # إنشاء اتصال بقاعدة البيانات باستخدام mysql.connector
    connection_mydb = mysql.connector.connect(
        host='localhost',  # اسم المضيف (السيرفر) حيث توجد قاعدة البيانات
        user='root',  # اسم المستخدم لقاعدة البيانات
        password='',  # كلمة المرور (في هذه الحالة، لا توجد كلمة مرور)
        database='wp-ecommerce'  # اسم قاعدة البيانات التي سيتم الاتصال بها
    )

    # إنشاء كائن المؤشر لتنفيذ الاستعلامات على قاعدة البيانات
    # تم تعيين dictionary=True ليكون الإخراج على شكل قاموس بدلاً من قائمة
    cursor = connection_mydb.cursor(dictionary=True)

    # إرجاع كلاً من الاتصال وكائن المؤشر
    return connection_mydb, cursor


def get_users_profiles():
    """
    استرجاع بيانات المستخدمين من قاعدة البيانات، بما في ذلك معرف المستخدم، الدولة، العمر، والجنس.
    """

    # إنشاء DataFrame لتخزين البيانات
    df = pd.DataFrame(columns=['user_id', 'country', 'age', 'gender'])

    # إنشاء الاتصال بقاعدة البيانات واسترجاع الكائنات المطلوبة
    _, cursor = make_connection_with_db()

    # جلب جميع معرفات المستخدمين من جدول wp_users
    sql = '''SELECT ID FROM `wp_users` WHERE 1'''
    cursor.execute(sql)
    users_results = cursor.fetchall()

    # التكرار عبر المستخدمين لجلب البيانات الإضافية
    for user in users_results:
        user_id = user['ID']

        # جلب الدولة للمستخدم
        sql = "SELECT meta_value FROM wp_usermeta WHERE user_id=(%s) and meta_key='country'"
        param = (user_id,)
        cursor.execute(sql, param)
        result = cursor.fetchall()
        country = result[0]['meta_value'] if result and len(result) > 0 else "Unknown"

        # جلب العمر للمستخدم
        sql = "SELECT meta_value FROM wp_usermeta WHERE user_id=(%s) and meta_key='age'"
        param = (user_id,)
        cursor.execute(sql, param)
        result = cursor.fetchall()
        age = result[0]['meta_value'] if result and len(result) > 0 else "Unknown"

        # جلب الجنس للمستخدم
        sql = "SELECT meta_value FROM wp_usermeta WHERE user_id=(%s) and meta_key='gender'"
        param = (user_id,)
        cursor.execute(sql, param)
        result = cursor.fetchall()
        gender = result[0]['meta_value'] if result and len(result) > 0 else "Unknown"

        # إنشاء كائن يحتوي على بيانات المستخدم
        obj = {
            'user_id': [user['ID']],
            'country': [country],
            'age': [age],
            'gender': [gender]
        }

        # تحويل البيانات إلى DataFrame ودمجها مع البيانات الأصلية
        df_obj = pd.DataFrame(obj)
        df = pd.concat([df, df_obj], ignore_index=True)

    # إزالة الصفوف التي تحتوي على بيانات غير معروفة
    df.drop(df[df['country'] == 'Unknown'].index, inplace=True)
    df.drop(df[df['age'] == 'Unknown'].index, inplace=True)
    df.drop(df[df['gender'] == 'Unknown'].index, inplace=True)

    # تحويل عمود العمر إلى نوع رقمي
    df['age'] = pd.to_numeric(df['age'])

    return df

