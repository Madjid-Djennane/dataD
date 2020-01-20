import { Component, OnInit } from '@angular/core';
declare var $: any;

@Component({
  selector: 'app-trafic',
  templateUrl: './trafic.component.html',
  styleUrls: ['./trafic.component.css']
})
export class TraficComponent implements OnInit {

  constructor() { }

  ngOnInit() {

    $('.datepicker').datetimepicker({
      format: 'DD-MM-YYYY HH:mm:ss'
    });

  }

}
