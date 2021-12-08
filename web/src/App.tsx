import { Component } from "react";
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import './App.css';

interface MyState {
  currentGame: any[][],
  turn: string
  xWinner: number,
  oWinner: number
}
class App extends Component<{}, MyState> {
  constructor(props: any) {
    super(props);

    // Initialize the array
    let currentGame: any[][] = []
    for (let i: number = 0; i < 3; i++) {
      currentGame[i] = [];
      for (let j: number = 0; j < 3; j++) {
        currentGame[i][j] = '';
      }
    }

    this.state = {
      currentGame: currentGame,
      turn: 'X',
      xWinner: 0,
      oWinner: 0
    };
  }

  cellClick = (row: number, col: number) => {
    const { currentGame, turn } = this.state;
    const cell = currentGame[row][col];
    if (cell === '') {
      currentGame[row][col] = turn;
      turn === 'X' ? this.setState({ turn: 'O' }) : this.setState({ turn: 'X' });
    }
  };

  restartGame = () => {
    // Do stuff
  }

  render() {
    const { currentGame, turn, xWinner, oWinner } = this.state;

    return (
      <Container className="p-3">
        <div className="h-100 p-5 bg-light border rounded-3">
          <h1 className="header">Tic Tac Toe</h1>
        </div>
        <div className="h-100 p-5 bg-light border rounded-3">
          <Row>
            <Col>
              <Card style={{ textAlign: 'right', fontWeight: 'bold' }} body>X Wins: {xWinner}</Card>
            </Col>
            <Col>
              <Card style={{ fontWeight: 'bold' }} body>O Wins: {oWinner}</Card>
            </Col>
          </Row>
          <Row>
            <Col>
              <h5>Turn: {turn}</h5>
            </Col>
          </Row>
          <table>
            <tbody>
              <tr>
                <td onClick={() => this.cellClick(0, 0)}>{currentGame[0][0]}</td>
                <td className="vert" onClick={() => this.cellClick(0, 1)}>{currentGame[0][1]}</td>
                <td onClick={() => this.cellClick(0, 2)}>{currentGame[0][2]}</td>
              </tr>
              <tr>
                <td className="hori" onClick={() => this.cellClick(1, 0)}>{currentGame[1][0]}</td>
                <td className="vert hori" onClick={() => this.cellClick(1, 1)}>{currentGame[1][1]}</td>
                <td className="hori" onClick={() => this.cellClick(1, 2)}>{currentGame[1][2]}</td>
              </tr>
              <tr>
                <td onClick={() => this.cellClick(2, 0)}>{currentGame[2][0]}</td>
                <td className="vert" onClick={() => this.cellClick(2, 1)}>{currentGame[2][1]}</td>
                <td onClick={() => this.cellClick(2, 2)}>{currentGame[2][2]}</td>
              </tr>
            </tbody>
          </table>
          <div>
            <Button className="center-align" variant="primary" onClick={this.restartGame}>Restart Game</Button>
          </div>
        </div>
      </Container>
    );
  }
}

export default App;
