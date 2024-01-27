from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from uuid import uuid4
import json

server_players = {
    # Key : Player UUID
    # Value : [x,y,orientation]
}

@csrf_exempt
def player_tracking(request):
    response = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        # Unique UUID
        player_id = data.get('uuid')
        # Float Coords
        player_x_pos = data.get('x_pos', 0)
        player_y_pos = data.get('y_pos', 0)
        # 0 Left, 1 Right
        player_orientation = data.get('orientation', 0)
        # If Player is not assigned an ID yet
        if not player_id:
            print('Generating ID')
            player_id = str(uuid4())
        server_players[player_id] = [player_x_pos, player_y_pos, player_orientation]
        response = {'player_positions': server_players, 'uuid': player_id}
    else:
        response = server_players
    return JsonResponse(response, safe=True)