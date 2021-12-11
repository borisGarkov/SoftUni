import unittest

from project.student import Student


class StudentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("Gogo")
        self.student_2 = Student("Sasho", {
            "Basics": ["test_1"],
            "Fundamentals": ["test_2"],
            "Advanced": ["test_3"]
        })

    def test_student_attributes(self):
        self.assertEqual(self.student.name, "Gogo")
        self.assertEqual(self.student.courses, {})

        self.assertEqual(self.student_2.name, "Sasho")
        self.assertEqual(self.student_2.courses, {
            "Basics": ["test_1"],
            "Fundamentals": ["test_2"],
            "Advanced": ["test_3"]
        })

    def test_if_course_name_in_courses_and_add_additional_notes_to_course_name(self):
        self.student_2.enroll("Basics", ["additional_test"])
        self.assertEqual(self.student_2.courses["Basics"], ["test_1", "additional_test"])
        self.assertEqual(self.student_2.enroll("Basics", ["additional_test"]),
                         "Course already added. Notes have been updated.")

    def test_add_course_notes(self):
        self.assertEqual(self.student.enroll("Basics", ["additional_test"]),
                         "Course and course notes have been added.")

    def test_add_course_notes_yes_string(self):
        self.assertEqual(self.student.enroll("Basics", ["additional_test"], "Y"),
                         "Course and course notes have been added.")

    def test_add_course_no_notes(self):
        self.assertEqual(self.student.enroll("Basics", [], "No"), "Course has been added.")
        self.assertEqual(self.student.courses, {'Basics': []})

    def test_enroll_add_new_course(self):
        enroll_course = self.student.enroll("AI", ["TensorFlow.", "PyTorch", "Scikit Learn"], "AI")
        self.assertEqual(self.student.courses, {"AI": []})
        self.assertEqual(enroll_course, "Course has been added.")

    def test_add_notes_to_course(self):
        self.assertEqual(self.student_2.add_notes("Basics", ["additional_test"]), "Notes have been updated")
        with self.assertRaises(Exception) as exc:
            self.student_2.add_notes("Web", ["additional_test"])
        self.assertEqual(str(exc.exception), "Cannot add notes. Course not found.")

    def test_leave_course(self):
        self.assertEqual(self.student_2.leave_course("Basics"), "Course has been removed")
        with self.assertRaises(Exception) as exc:
            self.student_2.leave_course("Web")
        self.assertEqual(str(exc.exception), "Cannot remove course. Course not found.")


if __name__ == '__main__':
    unittest.main()
