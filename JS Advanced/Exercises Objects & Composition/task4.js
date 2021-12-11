function compose(input) {
    let result = []

    for (const iterator of input) {
        let [hero, level, items] = iterator.split(' / ');
        level = Number(level);
        items = items ? items.split(', ') : [];

        current_obj = {
            name: hero,
            level: level,
            items: items,
        };

        result.push(current_obj)
    }
      
    console.log(JSON.stringify(result))
}

compose(['Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara']
)