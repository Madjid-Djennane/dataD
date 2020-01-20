import { Component, OnInit } from '@angular/core';
import { TraficService } from '../trafic.service';
declare var $: any;

@Component({
  selector: 'app-trafic',
  templateUrl: './trafic.component.html',
  styleUrls: ['./trafic.component.css']
})
export class TraficComponent implements OnInit {

  constructor(private traficService: TraficService) { }

  private date1 = '2015-12-12 18:25:11+01:00';
  private date2 = '2015-12-12 20:25:11+01:00';

  trafic = [];

  ngOnInit() {
    this.traficService.getTrafic(this.date1, this.date2)
      .subscribe(
        (data: string) => {
          this.trafic = JSON.parse(data);
        },
        err => {
          console.error(err);
        }
      );
  }

}
