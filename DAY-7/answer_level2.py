
def solution(record):
    nicknamedic = {rec.split(' ')[1]:rec.split(' ')[-1] for rec in record if rec.startswith('Enter') or rec.startswith('Change')}
    return [f"{nicknamedic[rec.split(' ')[1]]}님이 들어왔습니다." if rec.startswith('Enter') else f"{nicknamedic[rec.split(' ')[1]]}님이 나갔습니다." for rec in record if not rec.startswith('Change')]
