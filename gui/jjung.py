import tkinter as tk
from tkinter import filedialog, messagebox, Label
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import subprocess
import os


class YOLOv5GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YOLOv5 GUI")
        self.training_process = None
        self.weights_path = None
        self.image_paths = []

        self.current_image_index = 0
        self.photo_images = []

        # 홈 화면 구성
        self.home_frame = tk.Frame(root)
        self.home_frame.pack(fill="both", expand=True)
        tk.Label(self.home_frame, text="체크메이트 홈 화면", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.home_frame, text="1. 학습", command=self.open_train_window, width=20, height=2).pack(pady=10)
        tk.Button(self.home_frame, text="2. 탐지", command=self.open_detect_window, width=20, height=2).pack(pady=10)

        # 학습 화면 구성
        self.train_frame = tk.Frame(root)
        tk.Button(self.train_frame, text="뒤로가기", command=self.back_to_home).grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.train_frame, text="data.yaml 파일 선택:").grid(row=1, column=0, padx=10, pady=10)
        self.data_yaml_path = tk.Entry(self.train_frame, width=50)
        self.data_yaml_path.grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.train_frame, text="찾아보기", command=self.select_file).grid(row=1, column=2, padx=10, pady=10)
        tk.Label(self.train_frame, text="학습 파일 이름:").grid(row=2, column=0, padx=10, pady=10)
        self.model_name = tk.Entry(self.train_frame, width=50)
        self.model_name.grid(row=2, column=1, padx=10, pady=10)
        tk.Label(self.train_frame, text="저장할 디렉토리 선택:").grid(row=3, column=0, padx=10, pady=10)
        self.save_dir_path = tk.Entry(self.train_frame, width=50)
        self.save_dir_path.grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self.train_frame, text="찾아보기", command=self.select_directory).grid(row=3, column=2, padx=10, pady=10)

        tk.Label(self.train_frame, text="에포크 수 설정:").grid(row=4, column=0, padx=10, pady=10)
        self.epochs = tk.IntVar(value=1)
        self.epoch_slider = ttk.Scale(self.train_frame, from_=1, to=300, orient=tk.HORIZONTAL, variable=self.epochs,
                                      length=300)
        self.epoch_slider.grid(row=4, column=1, padx=10, pady=10)
        self.epoch_label = tk.Label(self.train_frame, text=f"{self.epochs.get()} 에포크")
        self.epoch_label.grid(row=4, column=2, padx=10, pady=10)
        self.epoch_slider.bind("<Motion>", self.update_epoch_label)

        tk.Button(self.train_frame, text="학습 시작", command=self.start_training).grid(row=5, column=1, padx=10, pady=20)

        self.progress_text = tk.Text(self.train_frame, height=10, width=80)
        self.progress_text.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

        # 탐지 화면 구성
        self.detect_frame = tk.Frame(root)
        tk.Button(self.detect_frame, text="뒤로가기", command=self.back_to_home_from_detect).grid(row=0, column=0, padx=10,
                                                                                              pady=10)
        tk.Button(self.detect_frame, text="이미지로 탐지", command=self.open_image_detect_window).grid(row=1, column=0,
                                                                                                 padx=10, pady=10)
        tk.Button(self.detect_frame, text="실시간 탐지", command=self.open_realtime_detect_window).grid(row=1, column=1,
                                                                                                   padx=10, pady=10)

        # 실시간 탐지 프레임 설정
        self.realtime_detect_frame = tk.Frame(root)
        tk.Button(self.realtime_detect_frame, text="뒤로가기", command=self.back_to_detect).grid(row=0, column=0, padx=10,
                                                                                             pady=10)
        tk.Button(self.realtime_detect_frame, text="모델 선택", command=self.select_model).grid(row=1, column=0, padx=10,
                                                                                            pady=10)
        tk.Button(self.realtime_detect_frame, text="실시간 탐지 시작", command=self.start_realtime_detection).grid(row=1,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=10)

        # 이미지 탐지 구성
        self.image_detect_frame = tk.Frame(root)
        tk.Button(self.image_detect_frame, text="뒤로가기", command=self.back_to_detect).grid(row=0, column=0, padx=10,
                                                                                          pady=10)
        self.image_list_frame = tk.Frame(self.image_detect_frame)
        self.image_list_frame.grid(row=1, column=0, columnspan=3)
        self.add_image_button = tk.Button(self.image_detect_frame, text="이미지 추가", command=self.add_image).grid(row=2,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=10)
        self.select_model_button = tk.Button(self.image_detect_frame, text="모델 선택", command=self.select_model).grid(
            row=2, column=1, padx=10, pady=10)
        self.start_detect_button = tk.Button(self.image_detect_frame, text="탐지 시작", command=self.start_detection).grid(
            row=2, column=2, padx=10, pady=10)

    def update_epoch_label(self, event):
        self.epoch_label.config(text=f"{self.epochs.get()} 에포크")

    def open_realtime_detect_window(self):
        self.detect_frame.pack_forget()
        self.realtime_detect_frame.pack(fill="both", expand=True)

    def start_realtime_detection(self):
        if not self.weights_path:
            messagebox.showwarning("경고", "먼저 모델을 선택하세요.")
            return
        command = f'python detect.py --source 0 --weights "{self.weights_path}" --conf 0.5'
        subprocess.Popen(command, shell=True)

    def add_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")])
        if file_path:
            self.image_paths.append(file_path)
            self.update_image_list()

    def select_model(self):
        file_path = filedialog.askopenfilename(title="모델 파일 선택",
                                               filetypes=[("Model files", "*.pt"), ("All files", "*.*")])
        if file_path:
            self.weights_path = file_path
            tk.Label(self.image_detect_frame, text=f"선택된 모델: {self.weights_path}").grid(row=3, column=0, columnspan=3)

    def start_detection(self):
        if not self.image_paths or not self.weights_path:
            messagebox.showwarning("경고", "이미지와 모델 파일을 먼저 추가하세요.")
            return
        result_directories = []

        for image_path in self.image_paths:
            command = f'python detect.py --source "{image_path}" --weights "{self.weights_path}" --conf 0.5 --project runs/detect --name exp'
            subprocess.run(command, shell=True)
            result_directories.append(self.get_latest_results_dir())

        self.display_results(result_directories)

    def get_latest_results_dir(self):
        base_path = 'runs/detect'
        all_subdirs = [os.path.join(base_path, d) for d in os.listdir(base_path) if
                       os.path.isdir(os.path.join(base_path, d))]
        if not all_subdirs:
            return None
        latest_subdir = max(all_subdirs, key=os.path.getmtime)
        return latest_subdir

    def display_results(self, folders):
        if not hasattr(self, 'result_window') or not self.result_window.winfo_exists():
            self.result_window = tk.Toplevel(self.root)
            self.result_window.title("Detection Results")
            self.photo_images = []
            self.prev_button = tk.Button(self.result_window, text="Previous", command=self.show_prev_image)
            self.prev_button.pack(side=tk.LEFT)
            self.next_button = tk.Button(self.result_window, text="Next", command=self.show_next_image)
            self.next_button.pack(side=tk.RIGHT)

        self.result_images = []
        for folder in folders:
            if folder is None:
                continue
            self.result_images += [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.jpg')]

        self.current_image_index = 0
        self.show_image()

    def show_image(self):
        if not self.result_images:
            messagebox.showinfo("Info", "No images to display.")
            return

        img_path = self.result_images[self.current_image_index]
        img = Image.open(img_path)
        img = img.resize((640, 640), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        self.photo_images.append(photo)

        if hasattr(self, 'image_label'):
            self.image_label.configure(image=photo)
        else:
            self.image_label = tk.Label(self.result_window, image=photo)
            self.image_label.image = photo
            self.image_label.pack()

    def show_next_image(self):
        if self.current_image_index < len(self.result_images) - 1:
            self.current_image_index += 1
            self.show_image()

    def show_prev_image(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.show_image()

    def update_image_list(self):
        for widget in self.image_list_frame.winfo_children():
            widget.destroy()
        for idx, path in enumerate(self.image_paths):
            tk.Label(self.image_list_frame, text=path).grid(row=idx, column=0)

    def open_train_window(self):
        self.home_frame.pack_forget()
        self.train_frame.pack(fill="both", expand=True)
        self.reset_train_window()

    def open_detect_window(self):
        self.home_frame.pack_forget()
        self.detect_frame.pack(fill="both", expand=True)

    def open_image_detect_window(self):
        self.image_paths.clear()
        self.weights_path = None
        self.detect_frame.pack_forget()
        self.image_detect_frame.pack(fill="both", expand=True)
        self.update_image_list()

    def back_to_home(self):
        if self.training_process and self.training_process.poll() is None:
            if messagebox.askyesno("경고", "학습이 진행 중입니다. 프로그램을 종료하시겠습니까?"):
                self.root.destroy()
            else:
                return
        else:
            self.train_frame.pack_forget()
            self.home_frame.pack(fill="both", expand=True)

    def back_to_home_from_detect(self):
        self.detect_frame.pack_forget()
        self.home_frame.pack(fill="both", expand=True)

    def reset_frames(self):
        for frame in [self.train_frame, self.detect_frame, self.image_detect_frame]:
            frame.pack_forget()
        self.home_frame.pack(fill="both", expand=True)

    def reset_train_window(self):
        self.data_yaml_path.delete(0, tk.END)
        self.model_name.delete(0, tk.END)
        self.save_dir_path.delete(0, tk.END)
        self.progress_text.delete(1.0, tk.END)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("YAML files", "*.yaml"), ("All files", "*.*")])
        self.data_yaml_path.delete(0, tk.END)
        self.data_yaml_path.insert(0, file_path)

    def select_directory(self):
        dir_path = filedialog.askdirectory()
        self.save_dir_path.delete(0, tk.END)
        self.save_dir_path.insert(0, dir_path)

    def start_training(self):
        data_yaml = self.data_yaml_path.get()
        model_name = self.model_name.get()
        save_dir = self.save_dir_path.get()
        epochs = self.epochs.get()
        if not data_yaml or not model_name or not save_dir:
            messagebox.showwarning("경고", "모든 필드를 입력해주세요.")
            return

        self.show_loading_screen()

        command = f'python train.py --img 640 --batch 16 --epochs {epochs} --data {data_yaml} --cfg models/yolov5s.yaml --weights yolov5s.pt --name {model_name} --project {save_dir}'
        self.training_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                                 text=True)
        threading.Thread(target=self.read_process_output).start()

    def show_loading_screen(self):
        self.loading_window = tk.Toplevel(self.root)
        self.loading_window.title("Loading")
        self.loading_window.geometry("300x200")
        self.loading_label = tk.Label(self.loading_window, text="학습 중입니다...\n잠시만 기다려주세요.", font=("Arial", 12))
        self.loading_label.pack(pady=20)
        gif_path = "icons/loading1.gif"
        self.loading_gif = [tk.PhotoImage(file=gif_path, format='gif -index %i' % i) for i in
                            range(30)]  # assuming 30 frames
        self.loading_gif_label = tk.Label(self.loading_window)
        self.loading_gif_label.pack()
        self.animate_gif(0)

    def animate_gif(self, ind):
        frame = self.loading_gif[ind]
        ind += 1
        if ind == len(self.loading_gif):
            ind = 0
        self.loading_gif_label.configure(image=frame)
        self.loading_window.after(50, self.animate_gif, ind)  # update every 50 ms

    def close_loading_screen(self):
        if hasattr(self, 'loading_window'):
            self.loading_window.destroy()

    def read_process_output(self):
        for line in self.training_process.stdout:
            self.progress_text.insert(tk.END, line)
            self.progress_text.see(tk.END)
        self.training_process.stdout.close()
        self.training_process.wait()
        self.close_loading_screen()
        if self.training_process.returncode == 0:
            messagebox.showinfo("완료", "학습이 완료되었습니다.")
        else:
            messagebox.showerror("오류", "학습 중 오류가 발생했습니다.")
        self.training_process = None

    def back_to_detect(self):
        self.realtime_detect_frame.pack_forget()
        self.image_detect_frame.pack_forget()
        self.detect_frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = YOLOv5GUI(root)
    root.mainloop()
