import math


def calculate_communication_rate(bandwidth, signal_power, noise_power):
    # 计算信噪比
    snr = signal_power / noise_power

    # 使用香农定理计算通信速率
    communication_rate = bandwidth * math.log2(1 + snr)

    return communication_rate


def calculate_signal_power(transmit_power, distance, obstacle_loss):
    # 计算实际信号功率，考虑了距离和障碍物衰减
    signal_power = transmit_power - (20 * math.log10(distance) + obstacle_loss)
    return 10 ** (signal_power / 10)  # 将信号功率从分贝转换为瓦特

def cal_comm_rate_use(distance, obstacle_loss):
    # 示例使用
    bandwidth = 10e6  # 带宽（单位：Hz），假设为200MHz
    transmit_power = 1  # 发送功率（单位：dBm），假设为1 dBm
    # distance = 100  # 通信距离（单位：米），假设为100米
    # obstacle_loss = 10  # 障碍物引起的信号损失（单位：dB），假设为10dB
    noise_power = 1e-6  # 噪声功率（单位：瓦特），假设为1μW

    # 计算信号功率
    signal_power = calculate_signal_power(transmit_power, distance, obstacle_loss)

    # 计算通信速率
    communication_rate = calculate_communication_rate(bandwidth, signal_power, noise_power)
    print("通信速率:", communication_rate / 1e6, "Mbps")  # 将速率转换为Mbps并打印出来

    return communication_rate / 1e6

if __name__ == '__main__':

    cal_comm_rate_use(100, 10)
