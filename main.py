            import json
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.metrics import dp


class DeathNotesApp(App):

    def build(self):
        self.title = "Death Notes"

        self.notes_file = os.path.join(
            self.user_data_dir,
            "notes.json"
        )

        self.notes = self.load_notes()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(8)
        )

        # عنوان التطبيق
        title = Label(
            text="Death Notes",
            font_size=dp(28),
            size_hint_y=None,
            height=dp(55)
        )
        root.add_widget(title)

        # عنوان المذكرة
        self.title_input = TextInput(
            hint_text="عنوان المذكرة...",
            multiline=False,
            font_size=dp(20),
            size_hint_y=None,
            height=dp(50)
        )
        root.add_widget(self.title_input)

        # محتوى المذكرة
        self.note_input = TextInput(
            hint_text="اكتب مذكرتك هنا...",
            font_size=dp(18),
            multiline=True
        )
        root.add_widget(self.note_input)

        # الأزرار
        buttons = BoxLayout(
            size_hint_y=None,
            height=dp(55),
            spacing=dp(6)
        )

        save_button = Button(text="حفظ")
        save_button.bind(on_press=self.save_note)

        open_button = Button(text="فتح")
        open_button.bind(on_press=self.show_notes)

        new_button = Button(text="جديد")
        new_button.bind(on_press=self.new_note)

        buttons.add_widget(save_button)
        buttons.add_widget(open_button)
        buttons.add_widget(new_button)

        root.add_widget(buttons)

        return root

    # تحميل المذكرات
    def load_notes(self):
        if not os.path.exists(self.notes_file):
            return {}

        try:
            with open(self.notes_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            return {}

    # حفظ جميع المذكرات
    def save_all_notes(self):
        os.makedirs(
            os.path.dirname(self.notes_file),
            exist_ok=True
        )

        with open(self.notes_file, "w", encoding="utf-8") as file:
            json.dump(
                self.notes,
                file,
                ensure_ascii=False,
                indent=2
            )

    # حفظ مذكرة
    def save_note(self, instance):
        title = self.title_input.text.strip()
        text = self.note_input.text

        if not title:
            self.show_message(
                "تنبيه",
                "اكتب عنوانًا للمذكرة أولًا."
            )
            return

        self.notes[title] = text
        self.save_all_notes()

        self.show_message(
            "تم الحفظ",
            "تم حفظ المذكرة بنجاح."
        )

    # إنشاء مذكرة جديدة
    def new_note(self, instance):
        self.title_input.text = ""
        self.note_input.text = ""

    # عرض المذكرات
    def show_notes(self, instance):
        if not self.notes:
            self.show_message(
                "المذكرات",
                "لا توجد مذكرات محفوظة."
            )
            return

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(5)
        )

        for title in self.notes:
            button = Button(
                text=title,
                size_hint_y=None,
                height=dp(50)
            )
            button.bind(
                on_press=lambda btn, t=title:
                self.open_note(t)
            )
            layout.add_widget(button)

        close_button = Button(
            text="إغلاق",
            size_hint_y=None,
            height=dp(50)
        )

        popup = Popup(
            title="مذكراتي",
            content=layout,
            size_hint=(0.9, 0.8)
        )

        close_button.bind(on_press=popup.dismiss)
        layout.add_widget(close_button)

        popup.open()

    # فتح مذكرة
    def open_note(self, title):
        self.title_input.text = title
        self.note_input.text = self.notes[title]

    # رسالة
    def show_message(self, title, message):
        layout = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(10)
        )

        label = Label(
            text=message,
            font_size=dp(18)
        )

        button = Button(
            text="حسنًا",
            size_hint_y=None,
            height=dp(50)
        )

        layout.add_widget(label)
        layout.add_widget(button)

        popup = Popup(
            title=title,
            content=layout,
            size_hint=(0.85, 0.4)
        )

        button.bind(on_press=popup.dismiss)

        popup.open()


if __name__ == "__main__":
    DeathNotesApp().run()
