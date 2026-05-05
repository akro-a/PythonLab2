import time
import wave
import numpy as np
import matplotlib.pyplot as plt

# Засекаем время начала работы программы
start_time = time.time()

# Вводим имя wav-файла
file_name = input("Введите имя wav-файла: ")

# Вводим количество первых отсчетов для первого графика
n = int(input("Введите количество первых отсчетов: "))

# Открываем wav-файл
wav_file = wave.open(file_name, "rb")

# Получаем частоту дискретизации
sample_rate = wav_file.getframerate()

# Получаем количество кадров
n_frames = wav_file.getnframes()

# Получаем количество каналов
n_channels = wav_file.getnchannels()

# Считываем все данные из файла
data = wav_file.readframes(n_frames)

# Закрываем файл
wav_file.close()

# Переводим байты в массив целых чисел
signal = np.frombuffer(data, dtype=np.int16)

# Если файл стерео, берем только один канал
if n_channels == 2:
    signal = signal[::2]

# Проверяем частоту дискретизации для варианта 7
if sample_rate != 44100:
    print("Ошибка: для варианта 7 нужна частота 44100 Гц")
else:
    print("Частота дискретизации:", sample_rate, "Гц")
    print("Количество отсчетов:", len(signal))

    # 1 график: первые N отсчетов
    plt.figure(figsize=(10, 4))
    plt.plot(signal[:n], linestyle="-")
    plt.title("Первые N отсчетов сигнала")
    plt.xlabel("Номер отсчета")
    plt.ylabel("Амплитуда")
    plt.grid()

    # 2 график: осциллограмма
    t = np.arange(len(signal)) / sample_rate

    plt.figure(figsize=(10, 4))
    plt.plot(t, signal, linestyle="-")
    plt.title("Осциллограмма сигнала")
    plt.xlabel("Время, с")
    plt.ylabel("Амплитуда")
    plt.grid()

    # 3 график: спектральный анализ
    x = np.fft.rfft(signal)
    spectrum = x.real ** 2 + x.imag ** 2
    freq = np.fft.rfftfreq(len(signal), 1 / sample_rate)

    plt.figure(figsize=(10, 4))
    plt.plot(freq, spectrum, linestyle="-")
    plt.title("Спектральный анализ: квадрат модуля ДПФ")
    plt.xlabel("Частота, Гц")
    plt.ylabel("Re^2 + Im^2")
    plt.grid()

    # 4 график: гистограмма
    plt.figure(figsize=(10, 4))
    plt.hist(signal, bins=50)
    plt.title("Гистограмма отсчетов сигнала")
    plt.xlabel("Амплитуда")
    plt.ylabel("Количество")
    plt.grid()

    # Показываем все графики сразу
    plt.show()

# Выводим время выполнения программы
print("Время выполнения программы:", time.time() - start_time, "seconds")