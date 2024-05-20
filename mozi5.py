
import os
import math
X=35
# 文字と記号のリスト（ひらがなとカタカナを追加）
characters = (#'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()=~|`{+*}<>?_-^\\@[;:],./\\'
              'オオオオオセセセセセ'
              'オオオオオセセセセセ'
              'オオオオわわセセセセ'
              'オオオわわわわセセセ'
              'オオオわわわわセセセ'
              'オオオわわわわセセセ'
              'オオオオわわセセセセ'
              'オオウウウウウウセセ'
              'ウウウウウウウウウウ'
             
              )

# 文字の個数に最も近い平方数を求める
num_chars = len(characters)
nearest_square = math.isqrt(num_chars) ** 2
if nearest_square < num_chars:
    nearest_square = (math.isqrt(num_chars) + 1) ** 2

# 平方数の平方根を求める
side_length = int(math.sqrt(nearest_square))
print(f'The nearest square number to {num_chars} is {nearest_square} with side length {side_length}.')

# 出力ディレクトリ名
output_dir = 'output_files'
os.makedirs(output_dir, exist_ok=True)

# 30行×270列の文字列を生成する関数
def generate_text(chars, num_chars_per_group):
    rows = []
    for start in range(0, len(chars), num_chars_per_group):
        group_chars = chars[start:start + num_chars_per_group]
        for _ in range(X):
            row = ''.join(char * X for char in group_chars)
            rows.append(row)
            if len(rows) >= X:
                yield '\n'.join(rows)
                rows = []
    if rows:
        yield '\n'.join(rows)

# テキスト生成とファイルへの書き込み
output_file = os.path.join(output_dir, f'output{X}.txt')
num_chars_per_group = side_length

with open(output_file, 'w', encoding='utf-8') as file:
    for text_chunk in generate_text(characters, num_chars_per_group):
        file.write(text_chunk + '\n')  

print(f'Text data has been written to {output_file}')
