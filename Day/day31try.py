def bmp_info(data):
    m = struct.unpack('<ccIIIIIIHH', data[:30])
    print(m)
    return {
        'width': m[6],
        'height': m[7],
        'color': m[9]
    }

# 将图片写入文件，看看长什么样的
with open('bmp.bmp', 'wb') as f:
    f.write(bmp_data)

# 试试这样能不能读
with open('bmp.bmp', 'rb') as f:
    bmp_info(f.read(30))

# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')
