import 'package:flutter/material.dart';
import 'package:game_vault/%20widgets/app_drawer.dart';

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
        body: TabBarView
        (
          children: 
          [
            const Center(child: Text('Aquí irán los juegos')),
            const Center(child: Text('Aquí irán los favoritos')),
            const Center(child: Text('Aquí irán las categorías')),
          ],
        ),
        drawer: AppDrawer(),
      ),
    );
  }
}