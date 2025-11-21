import 'package:flutter/material.dart';
import 'package:game_vault/%20widgets/app_drawer.dart';
import 'package:game_vault/ widgets/games_grid.dart';
import 'package:game_vault/ widgets/categories_list.dart';
import 'package:game_vault/ widgets/add_game_screen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) 
  {
    return DefaultTabController
    (
      length: 3,
      child: Scaffold
      (
        appBar: AppBar
        (
          title: const Text('GameVault'),
          actions: const 
          [
            Icon(Icons.search),
            SizedBox(width: 30),
            Icon(Icons.more_vert),
            SizedBox(width: 40),
          ],
          bottom: const TabBar
          (
            tabs: 
            [
              Tab(icon: Icon(Icons.videogame_asset), text: 'Juegos'),
              Tab(icon: Icon(Icons.star), text: 'Favoritos'),
              Tab(icon: Icon(Icons.category), text: 'Categorías'),
            ],
          ),
        ),
        floatingActionButton: FloatingActionButton
        (
          child: const Icon(Icons.add),
          onPressed: () async 
          {
            final resultado = await Navigator.push
            (
              context, 
              MaterialPageRoute(builder: (_) => const AddGameScreen())
            );
          },
        ),
        body: TabBarView
        (
          children: 
          [
            const GamesGrid(),
            const Center(child: Text('Aquí irán los favoritos')),
            const CategoriesList()
          ],
        ),
        drawer: AppDrawer(),
      ),
    );
  }
}