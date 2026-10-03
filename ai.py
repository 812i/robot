import streamlit as st

# إعداد الصفحة وتوسيع العرض لتكون مرتبة
st.set_page_config(page_title="Medical Robotics Portal", page_icon="⚕️", layout="wide")

# ترويسة رئيسية جذابة
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>⚕️ البوابة التذكارية للروبوتات الطبية الحديثة</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #566573;'>استعراض شامل لأبرز التقنيات والروبوتات المتقدمة في القطاع الصحي والعمليات الجراحية</p>", unsafe_allow_html=True)
st.markdown("---")

# تقسيم الصفحة إلى أقسام باستخدام البطاقات المنظمة
st.markdown("### 🤖 اختر الروبوت الطبي للاستكشاف:")
robot_choice = st.selectbox(
    "القائمة التفاعلية:",
    [
        "روبوت دافنشي (Da Vinci Surgical System)",
        "روبوت روزا (ROSA Brain & Spine Robot)",
        "روبوت مابور (Mako SmartRobotics)",
        "روبوتات التأهيل والعلاج الطبيعي (Exoskeletons)"
    ],
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)

# عرض المعلومات داخل حاويات (Containers) مرتبة وبشكل بطاقات
with st.container():
    if robot_choice == "روبوت دافنشي (Da Vinci Surgical System)":
        st.subheader("🔹 1. روبوت دافنشي للجراحات الدقيقة")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**📌 النوع:**")
            st.info("نظام جراحي بمساعدة الحاسوب وعن بُعد (Computer-assisted Surgical System).")
            
            st.markdown("**⚙️ طريقة العمل:**")
            st.success("يجلس الجراح على وحدة تحكم مرئية ثلاثية الأبعاد (3D HD)، وتترجم حركات يديه بدقة متناهية إلى أدوات دقيقة داخل جسم المريض، مع إلغاء أي رجفة طبيعية في يد الإنسان.")
            
        with col2:
            st.markdown("**💡 الفائدة الطبية:**")
            st.warning("إجراء عمليات معقدة (مثل جراحات المسالك البولية والقلب والنساء) من خلال شقوق جراحية مجهرية صغرى، مما يقلل النزيف، يسرع الشفاء، ويقلل فترة بقاء المريض بالمستشفى.")

    elif robot_choice == "روبوت روزا (ROSA Brain & Spine Robot)":
        st.subheader("🔹 2. روبوت روزا لجراحات المخ والأعصاب والعمود الفقري")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**📌 النوع:**")
            st.info("مساعد جراحي عصبي ذكي مزود بنظام توجيه بالأشعة.")
            
            st.markdown("**⚙️ طريقة العمل:**")
            st.success("يعمل كذراع روبوتي يوجه الجراح بدقة مذهلة بناءً على خرائط دماغية ثلاثية الأبعاد مسبقة التصوير للمريض، لتحديد إحداثيات العمليات بدقة تصل لأجزاء من المليمتر.")
            
        with col2:
            st.markdown("**💡 الفائدة الطبية:**")
            st.warning("تقليل وقت الجراحة بشكل كبير في العمليات الدقيقة جداً مثل جراحات الصرع وإزالة أورام الدماغ بدقة بالغة ودون الإضرار بالأنسجة السليمة.")

    elif robot_choice == "روبوت مابور (Mako SmartRobotics)":
        st.subheader("🔹 3. روبوت ميكو لجراحات العظام والمفاصل")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**📌 النوع:**")
            st.info("ذراع روبوتي تفاعلي متخصص في استبدال المفاصل (الركبة والورك).")
            
            st.markdown("**⚙️ طريقة العمل:**")
            st.success("يضع الجراح خطة جراحية افتراضية مسبقة لكل مريض، ويقوم الذراع الروبوتي بمساعدة الجراح على إزالة العظام التالفة بدقة مطابقة للخطة المرسومة تماماً مع منع الجراح من تجاوز الحدود الآمنة.")
            
        with col2:
            st.markdown("**💡 الفائدة الطبية:**")
            st.warning("تحقيق محاذاة أدق للمفصل الصناعي، تقليل الألم بعد العملية، وزيادة العمر الافتراضي للمفصل المزروع.")

    elif robot_choice == "روبوتات التأهيل والعلاج الطبيعي (Exoskeletons)":
        st.subheader("🔹 4. الهياكل الخارجية لتأهيل الأطراف")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**📌 النوع:**")
            st.info("هيكل روبوتي قابل للارتداء (Wearable Robotic Exoskeleton).")
            
            st.markdown("**⚙️ طريقة العمل:**")
            st.success("يتم تثبيته على أطراف المريض المصاب بشلل أو ضعف عضلي، وتعمل المستشعرات الذكية على استشعار نية الحركة لدى المريض ومساعدته آلياً على تحريك الساقين أو الذراعين.")
            
        with col2:
            st.markdown("**💡 الفائدة الطبية:**")
            st.warning("مساعدة المرضى على استعادة القدرة على المشي، وتحفيز الجهاز العصبي على التعافي السريع أثناء جلسات العلاج الطبيعي.")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>تم تطوير هذا التطبيق خصيصاً لمقرر الروبوتات 🤍</p>", unsafe_allow_html=True)
